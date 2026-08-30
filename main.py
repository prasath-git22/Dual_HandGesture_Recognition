import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import pygetwindow as gw
import json
from collections import deque

# Optional brightness control
try:
    import screen_brightness_control as sbc
    BRIGHTNESS_AVAILABLE = True
except:
    BRIGHTNESS_AVAILABLE = False

# ======================
# LOAD CONFIG (OPTIONAL)
# ======================
try:
    with open("gestures.json") as f:
        gesture_map = json.load(f)
except:
    gesture_map = {}

# ======================
# SCREEN
# ======================
screen_w, screen_h = pyautogui.size()

# ======================
# MEDIAPIPE
# ======================
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)
mp_draw = mp.solutions.drawing_utils

# ======================
# CAMERA
# ======================
cap = cv2.VideoCapture(0)

# ======================
# CONTROL
# ======================
smoothening = 5
plocX, plocY = 0, 0

gesture_buffer = deque(maxlen=7)     # right hand
control_buffer = deque(maxlen=5)     # left hand (NEW)

last_action = 0
cooldown = 0.6
dragging = False
prev_y = 0

# ======================
# MODE DETECTION
# ======================
def get_mode():
    try:
        win = gw.getActiveWindow()
        if win:
            title = win.title.lower()
            if "powerpoint" in title:
                return "ppt"
            elif "vlc" in title or "youtube" in title:
                return "media"
            elif "chrome" in title or "edge" in title:
                return "browser"
    except:
        pass
    return "mouse"

# ======================
# FINGER DETECTION
# ======================
def fingers_up(lm):
    fingers = []
    fingers.append(1 if lm[4][0] > lm[3][0] else 0)
    tips = [8, 12, 16, 20]
    for tip in tips:
        fingers.append(1 if lm[tip][1] < lm[tip-2][1] else 0)
    return fingers

# ======================
# MAIN LOOP
# ======================
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    overlay = np.zeros_like(img)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    hand_data = []

    if results.multi_hand_landmarks and results.multi_handedness:
        for handLms, handedness in zip(results.multi_hand_landmarks,
                                       results.multi_handedness):

            label = handedness.classification[0].label
            lm_list = [(int(lm.x*w), int(lm.y*h)) for lm in handLms.landmark]

            hand_data.append((label, lm_list))

            mp_draw.draw_landmarks(
                overlay,
                handLms,
                mp_hands.HAND_CONNECTIONS
            )

    move_hand = None
    control_hand = None

    for label, lm_list in hand_data:
        if label == "Right":
            move_hand = lm_list
        elif label == "Left":
            control_hand = lm_list

    mode = get_mode()
    gesture = "NONE"

    # ======================
    # RIGHT HAND → MOUSE
    # ======================
    if move_hand:
        f = fingers_up(move_hand)
        gesture_buffer.append(tuple(f))
        stable = max(set(gesture_buffer), key=gesture_buffer.count)

        x, y = move_hand[8]

        screenX = np.interp(x, (0, w), (0, screen_w))
        screenY = np.interp(y, (0, h), (0, screen_h))

        clocX = plocX + (screenX - plocX) / smoothening
        clocY = plocY + (screenY - plocY) / smoothening
        plocX, plocY = clocX, clocY

        if stable == (0,1,0,0,0):
            pyautogui.moveTo(clocX, clocY)
            gesture = "MOVE"

        elif stable == (0,1,1,0,0):
            if time.time() - last_action > cooldown:
                pyautogui.click()
                last_action = time.time()
            gesture = "CLICK"

        elif stable == (0,0,0,0,0):
            if not dragging:
                pyautogui.mouseDown()
                dragging = True
            gesture = "DRAG"

        else:
            if dragging:
                pyautogui.mouseUp()
                dragging = False

    # ======================
    # LEFT HAND → CONTROL (FIXED)
    # ======================
    if control_hand:

        f = fingers_up(control_hand)
        control_buffer.append(tuple(f))
        f = max(set(control_buffer), key=control_buffer.count)  # STABLE

        if time.time() - last_action > cooldown:

            key = str(list(f))

            # CONFIG OVERRIDE
            if key in gesture_map.get(mode, {}):
                action = gesture_map[mode][key]

                if action == "forward":
                    pyautogui.press("right")
                elif action == "backward":
                    pyautogui.press("left")
                elif action == "play":
                    pyautogui.press("space")
                elif action == "minimize":
                    pyautogui.hotkey("win", "down")
                elif action == "maximize":
                    pyautogui.hotkey("win", "up")
                elif action == "new_tab":
                    pyautogui.hotkey("ctrl", "t")
                elif action == "close_tab":
                    pyautogui.hotkey("ctrl", "w")

                gesture = action.upper()

            else:
                # ===== MEDIA =====
                if mode == "media":

                    if f == (0,1,0,0,0):
                        pyautogui.press("right")
                        gesture = "FORWARD"

                    elif f == (0,0,0,0,0):
                        pyautogui.press("left")
                        gesture = "BACKWARD"

                    elif f == (0,1,1,0,0):
                        pyautogui.press("space")
                        gesture = "PLAY"

                    elif f == (0,1,1,1,0):
                        pyautogui.hotkey("win","down")
                        gesture = "MINIMIZE"

                    elif f == (1,0,0,0,1):
                        pyautogui.hotkey("win","up")
                        gesture = "MAXIMIZE"

                    elif f == (1,0,0,0,0):
                        pyautogui.press("volumeup")
                        gesture = "VOL UP"

                    elif f == (0,0,0,0,1):
                        pyautogui.press("volumedown")
                        gesture = "VOL DOWN"

                # ===== PPT =====
                elif mode == "ppt":

                    if f == (1,0,0,0,0):
                        pyautogui.press("right")
                        gesture = "NEXT"

                    elif f == (0,0,0,0,1):
                        pyautogui.press("left")
                        gesture = "PREV"

                    elif f == (0,0,0,0,0):
                        pyautogui.press("esc")
                        gesture = "EXIT"

                    elif f == (1,1,1,1,1):
                        pyautogui.press("f5")
                        gesture = "START"

                # ===== BROWSER =====
                elif mode == "browser":

                    if f == (0,1,1,0,0):
                        pyautogui.hotkey("ctrl","t")
                        gesture = "NEW TAB"

                    elif f == (0,1,1,1,0):
                        pyautogui.hotkey("ctrl","w")
                        gesture = "CLOSE TAB"

                # ===== DEFAULT =====
                else:

                    if f == (0,1,1,0,0):
                        pyautogui.hotkey("ctrl","c")
                        gesture = "COPY"

                    elif f == (0,1,1,1,0):
                        pyautogui.hotkey("ctrl","v")
                        gesture = "PASTE"

            # ===== BRIGHTNESS (FIXED)
            if BRIGHTNESS_AVAILABLE and f == (1,1,0,0,0):
                if prev_y != 0:
                    if control_hand[8][1] < prev_y - 10:
                        sbc.set_brightness('+5')
                        gesture = "BRIGHT UP"
                    elif control_hand[8][1] > prev_y + 10:
                        sbc.set_brightness('-5')
                        gesture = "BRIGHT DOWN"

                prev_y = control_hand[8][1]

            last_action = time.time()

    # ======================
    # UI
    # ======================
    cv2.putText(overlay, "AI SYSTEM",
                (20,30), 0, 0.8, (0,255,255), 2)

    cv2.putText(overlay, f"MODE: {mode.upper()}",
                (400,30), 0, 0.7, (255,255,0), 2)

    cv2.putText(overlay, f"GESTURE: {gesture}",
                (20,70), 0, 0.7, (0,255,0), 2)

    cv2.imshow("FINAL SYSTEM", overlay)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
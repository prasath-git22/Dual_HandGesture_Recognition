import cv2
import mediapipe as mp
import csv

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

gesture_label = input("Enter gesture name: ")

with open("gesture_data.csv", "a", newline="") as f:
    writer = csv.writer(f)

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                row = []

                base_x = handLms.landmark[0].x
                base_y = handLms.landmark[0].y

                for lm in handLms.landmark:
                    row.append(lm.x - base_x)
                    row.append(lm.y - base_y)

                row.append(gesture_label)
                writer.writerow(row)

        cv2.imshow("Collect Data", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
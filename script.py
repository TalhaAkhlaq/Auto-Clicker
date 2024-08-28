import pyautogui
import threading
from pynput import keyboard
import time
import sys  

refresh_button = None
register_button = None
pixel_position = None
refresh_page_button = None

pyautogui.PAUSE = 0

active = False

def color_difference(color1, color2):
    """Calculate the Euclidean distance between two RGB colors."""
    return sum((a - b) ** 2 for a, b in zip(color1, color2)) ** 0.5

def click_loop():
    """Continuously click two specified buttons on the screen with minimal delay."""
    while True:
        if active:
            pyautogui.click(refresh_button)
            pyautogui.click(register_button)
        else:
            time.sleep(0.1)  

def monitor_pixel():
    """Monitor a pixel for color changes and click a button if a change is detected."""
    global pixel_position, refresh_page_button
    initial_color = pyautogui.pixel(pixel_position[0], pixel_position[1])
    while True:
        if active:
            current_color = pyautogui.pixel(pixel_position[0], pixel_position[1])
            if color_difference(current_color, initial_color) > 10:
                pyautogui.click(refresh_page_button)  
                while color_difference(pyautogui.pixel(pixel_position[0], pixel_position[1]), initial_color) > 10:
                    time.sleep(0.1)
                initial_color = pyautogui.pixel(pixel_position[0], pixel_position[1])

def on_press(key):
    """Handle keyboard inputs to control the automation."""
    global active
    if key == keyboard.Key.esc:
        return  
    try:
        if hasattr(key, 'char'):
            if key.char == 's':
                active = not active
                print("Program started." if active else "Program paused.")
            elif key.char == 'q':
                print("Quit command received, stopping the program...")
                sys.exit(0)
            elif key.char == 'r':
                if active:  
                    active = False
                    print("Program paused for resetting...")
                print("Resetting setup...")
                setup_positions()  
    except AttributeError:
        pass  

def setup_positions():
    """Set up positions for mouse actions by user input, only Enter key confirms positions."""
    global refresh_button, register_button, pixel_position, refresh_page_button
    input("Hover over the Refresh button and press Enter to confirm.")
    refresh_button = pyautogui.position()
    input("Hover over the Register Now button and press Enter to confirm.")
    register_button = pyautogui.position()
    input("Hover over the pixel to monitor and press Enter to confirm.")
    pixel_position = pyautogui.position()
    input("Hover over the Refresh Page button and press Enter to confirm.")
    refresh_page_button = pyautogui.position()
    print("Setup complete. Press 's' to start/pause the automation, 'r' to redo setup, and 'q' to quit the program.")

def main():
    """Initialize the program by setting up positions and starting threads."""
    setup_positions()
    click_thread = threading.Thread(target=click_loop, daemon=True)
    pixel_thread = threading.Thread(target=monitor_pixel, daemon=True)
    click_thread.start()
    pixel_thread.start()

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

if __name__ == "__main__":
    main()
    
    
    
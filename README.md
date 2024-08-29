# Auto-Clicker

This is an auto-clicker program written in Python that automates clicking on specified buttons on the screen and monitors a pixel for color changes to trigger additional actions.

## Features

- **Automated Clicking**: Continuously clicks specified buttons on the screen.
- **Pixel Monitoring**: Monitors a specific pixel for color changes and triggers actions based on those changes.
- **Keyboard Controls**: Start, pause, reset, and exit the program using keyboard shortcuts.

## Getting Started

To get started with this auto-clicker program, follow the steps below to set up and use it:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/auto-clicker.git
    cd auto-clicker
    ```

2. **Install the required libraries**:
    ```bash
    pip install pyautogui pynput
    ```

3. **Run the program**:
    ```bash
    python auto_clicker.py
    ```

## Usage

1. **Run the program**:
    ```bash
    python auto_clicker.py
    ```

2. **Setup Positions**: Follow on-screen instructions to set up positions:
   - Hover over the `Reload` button and press Enter.
   - Hover over the button you would like to auto-click on and press Enter.
   - Hover over the pixel to monitor and press Enter.
   - Hover over another button you want to trigger when the pixel color changes and press Enter.

3. **Keyboard Controls**:
   - Press `s` to start or pause the automation.
   - Press `r` to redo the setup positions.
   - Press `q` to quit the program.

## Instructions

- **Main Functions**:
  - `click_loop()`: Continuously clicks the specified buttons when active.
  - `monitor_pixel()`: Monitors a pixel for color changes and clicks the associated button if a change is detected.
  - `on_press()`: Handles keyboard inputs for starting, pausing, resetting, and exiting the program.

- **Program Flow**:
  - The program begins by prompting the user to set up button and pixel positions.
  - Two threads are started: one for the click loop and one for pixel monitoring.
  - Keyboard inputs are handled in real-time to control the program.

## Notes

- This program requires administrative privileges for screen control.
- Use caution when running the auto-clicker, as it may interfere with other screen interactions.

## Disclaimer

Use this program responsibly. The author is not liable for any misuse or damage caused by running this software.

## Copyright & Licensing

Copyright (C) 2024 Talha Akhlaq <talhaakhlaq1@gmail.com>

Distributed under the MIT License. See `LICENSE` for details.
#
For more information on my projects and other academic work, please visit my [GitHub profile](https://github.com/TalhaAkhlaq).


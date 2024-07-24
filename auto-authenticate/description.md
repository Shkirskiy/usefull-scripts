# Auto-Authenticate Script for AZERTY Keyboard

## Description
This Python script automates the process of entering a password into a pop-up authentication window on a system using a French AZERTY keyboard layout. It periodically checks for the presence of the pop-up window and, if detected, automatically fills in the password and clicks the authentication button.

## Features
- Periodically checks for an authentication pop-up window using image recognition.
- Automatically types in the password using the correct key mappings for a French AZERTY keyboard layout.
- Clicks the authenticate button to submit the password.

## Dependencies
- `pyautogui`
- `pyscreenshot`
- `time`
- `opencv-python-headless` (for confidence level in `pyautogui.locate`)

## Usage
1. Ensure you have the necessary dependencies installed:
   ```bash
   pip install pyautogui pyscreenshot opencv-python-headless


Feel free to customize the description as needed for your specific use case. This description provides a clear understanding of what the script does and how to use it.

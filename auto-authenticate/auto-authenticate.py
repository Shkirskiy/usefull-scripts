import pyautogui
import pyscreenshot as ImageGrab
import time

# Replace 'password' with your actual password
PASSWORD = "password"
# Screenshot of the pop-up window or a unique part of it to identify the pop-up
POPUP_IMAGE = "screen_login.png"
# Coordinates of the password input field (these need to be determined manually)
PASSWORD_FIELD_COORDS = (x, y)  # Replace with actual coordinates
# Coordinates of the authenticate button
AUTH_BUTTON_COORDS = (x, y)  # Replace with actual coordinates

def check_for_popup():
    print("Taking a screenshot of the current screen...")
    screenshot = ImageGrab.grab()
    screenshot_path = 'current_screenshot.png'
    screenshot.save(screenshot_path)
    print(f"Screenshot saved at {screenshot_path}")

    try:
        print(f"Checking if the pop-up image is in the screenshot with confidence level...")
        location = pyautogui.locate(POPUP_IMAGE, screenshot_path, confidence=0.8)
        if location:
            print(f"Pop-up found at location: {location}")
            return True
        else:
            print("Pop-up not found.")
            return False
    except pyautogui.ImageNotFoundException:
        print("ImageNotFoundException: Could not locate the image.")
        return False

def simulate_typing_azerty(password):
    key_mapping = {
        '0': 'à',
        '1': '&',
        '2': 'é',
        '3': '"',
        '4': "'",
        '5': '(',
        '6': '-',
        '7': 'è',
        '8': '_',
        '9': 'ç'
    }
    
    for char in password:
        if char in key_mapping:
            print(f"Pressing: {key_mapping[char]} for {char}")
            pyautogui.keyDown('shift')
            pyautogui.press(char)
            pyautogui.keyUp('shift')
        else:
            print(f"Pressing: {char}")
            pyautogui.press(char)
        time.sleep(0.1)  # Add a short delay between key presses

def fill_password_and_authenticate():
    print("Filling in the password and clicking authenticate...")
    pyautogui.click(PASSWORD_FIELD_COORDS)
    time.sleep(0.5)  # Short delay to ensure the click is registered
    simulate_typing_azerty(PASSWORD)  # Use the updated typing function
    time.sleep(0.5)  # Short delay to ensure the typing is completed
    pyautogui.click(AUTH_BUTTON_COORDS)
    print("Password filled and authenticate button clicked.")

def main():
    print("Starting the main loop...")
    while True:
        if check_for_popup():
            fill_password_and_authenticate()
        else:
            print("Pop-up not detected, waiting for 5 seconds before retrying...")
        # Wait for a while before checking again
        time.sleep(5)

if __name__ == "__main__":
    main()

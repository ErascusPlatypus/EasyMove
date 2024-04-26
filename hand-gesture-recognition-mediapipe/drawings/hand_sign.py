import webbrowser
import time
import pyautogui as auto

time_file_path = "last_zero_detection_time.txt"

def get_last_zero_detection_time():
    try:
        with open(time_file_path, 'r') as file:
           content = file.read().strip()
           if content:
                return float(content)
           else:
                return 0
    except FileNotFoundError:
        return 0

def update_last_zero_detection_time(time_value):
    with open(time_file_path, 'w') as file:
        file.write(str(time_value))

def detect_hand_sign(hand_sign_id):
    last_zero_detection_time = get_last_zero_detection_time()

    current_time = time.time()
    time_difference = current_time - last_zero_detection_time

    if hand_sign_id == 1 and time_difference > 15:
        auto.click()
        update_last_zero_detection_time(current_time)
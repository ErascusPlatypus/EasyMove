import time
import pyautogui as auto
from drawings import landmarks
import math 
import numpy as np 

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

def detect_hand_sign(hand_sign_id, landmark_list, prev_hand_sign):
    last_zero_detection_time = get_last_zero_detection_time()

    current_time = time.time()
    time_difference = current_time - last_zero_detection_time

    if prev_hand_sign != 3 or hand_sign_id != 3 :  
        # print("here")
        auto.keyUp('altLeft')

    if hand_sign_id == 1 and time_difference > 5:
        prev_hand_sign = 1 
        auto.click()
        update_last_zero_detection_time(current_time)

    elif(hand_sign_id == 4):
        prev_hand_sign = 4
        auto.scroll(120)
    elif hand_sign_id == 7 and time_difference > 3 : 
        auto.scroll(-120)

    elif hand_sign_id == 3 :              
        # Simulate pressing the "tab" key additional times based on tabs_to_press
        if(prev_hand_sign == 3) :
            auto.press('tab')
            time.sleep(0.5)  # Wait for 0.5 seconds between tab presses
        else : 
            auto.keyDown('altleft')  # Press and hold the Alt key
            auto.press('tab')

        prev_hand_sign = 3

        # auto.keyUp('altleft')  # Release the Alt key

    elif hand_sign_id == 10:
        if(prev_hand_sign == 10) :
            auto.press('tab')
            time.sleep(0.5)
        else:
            auto.keyDown('ctrlleft')
            auto.press('tab')

        prev_hand_sign = 10

    elif(hand_sign_id == 2):
        prev_hand_sign = 2 
        ######################### Moving Cursor in direction of pointer ###############################

        wrist_point = landmark_list[0]
        index_point = landmark_list[8]

        distance_vector = np.array([index_point[0] - wrist_point[0] , index_point[1] - wrist_point[1]])

        angle_degrees = math.degrees(math.atan2(distance_vector[1], distance_vector[0]))
        if angle_degrees < 0:
            angle_degrees += 360

        cursor_speed = 40  # Adjust cursor speed as needed
        cursor_move_x = cursor_speed * math.cos(math.radians(angle_degrees))
        cursor_move_y = cursor_speed * math.sin(math.radians(angle_degrees))
        auto.move(cursor_move_x, cursor_move_y)
                
        ################################################################################################
    else :
        prev_hand_sign = 0



    return prev_hand_sign
Project Update

- Added functionalities :
    - Move cursor on screen according to gesture : 
        - Currently, for any hand gesture, the cursor moves by finding a distance vector from the coordinates of the tip of the 
        index finger (landmark_list[8]) and the wrist point(landmark_list[0]). It uses this to find the direction to move.
        
        TO FIX : 
            - The cursor movement is glitchy / low framerate, find a way to improve it 
            - Fist / Close gesture is currently mapped to click on screen. But, even if it detects this gesture for just one 
              frame, it leads to a click on screen causing a lot of accidental clicks. Make it so that only if the gesture is 
              detected for "x" frames or say 1 second, it clicks. 
            - The cursor movement works for all gestures currently. So regardless of what you make, it will detect the index 
              and wrist coordinates and make the corresponding movement on screen. Only move the cursor when you make the 
              pointer gesture.
    
    - Cleaned up the code : 
        - Moved the draw_landmarks code to a seperate file to make the main (app.py) file cleaner.
        - Moved all click / pyautogui functions to a seperate file

        TO FIX : 
            - Further clear up main file. Lots of code that can be moved to a seperate file.
            - Cursor Movement gestures are in the main code. Move them to a seperate file or hand_sign.py with other gestures

    - Added more gestures : 
        - Added gestures to detect : 
            - Two
            - Three
            - Four
            - Five 
            - Thumbs Up 
            - Thumbs Down
            - One-Yo
            - Two-Yo
            
            with pre-existing gestures for : 
            - pointer
            - ok 
            - close 
            - five
                 

import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

from utils.state import gesture_active, program_running
from config.settings import *

pyautogui.FAILSAFE = False

def run_gesture_control():
    wScr, hScr = pyautogui.size()

    plocX, plocY = 0, 0
    clocX, clocY = 0, 0
    last_click_time = 0
    last_zoom_time = 0
    dragging = False

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1,
                           min_detection_confidence=0.7,
                           min_tracking_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)

    while program_running.is_set():
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0].landmark

            if gesture_active.is_set():
                ix, iy = int(lm[8].x * w), int(lm[8].y * h)
                tx, ty = int(lm[4].x * w), int(lm[4].y * h)
                mx, my = int(lm[12].x * w), int(lm[12].y * h)
                px, py = int(lm[20].x * w), int(lm[20].y * h)
                p_base_y = int(lm[17].y * h)

                x3 = np.interp(ix, (frameR, w-frameR), (0, wScr))
                y3 = np.interp(iy, (frameR, h-frameR), (0, hScr))

                clocX = plocX + (x3 - plocX)/smoothening
                clocY = plocY + (y3 - plocY)/smoothening

                pyautogui.moveTo(clocX, clocY)

                plocX, plocY = clocX, clocY

                current_time = time.time()
                dist = np.hypot(ix - tx, iy - ty)

                if dist < click_threshold:
                    pyautogui.click()

        cv2.imshow("Gesture Control", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            program_running.clear()
            break

    cap.release()
    cv2.destroyAllWindows()

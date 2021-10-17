import cv2 as cv
import time
import math
from subprocess import call
import platform
import osascript

import hand_detector_module as hand_detector

# Capturing vid (change filename to 0 if need webcam)
capture = cv.VideoCapture('videos/hand_vid_test.3gp')

pTime = 0
detector = hand_detector.HandDetector()

while True:
    # Reading currunt img
    success, img = capture.read()

    # If can't read currunt img, break loop
    if not success:
          break

    # Detecting hand
    detector.detectHands(img, draw=False)

    # Getting positions of landmarks in detected hand
    lmsList = detector.findPos(img, draw=False)

    if len(lmsList) != 0:
        # Getting coordinates of thumb and index finger tips
        x1, y1 = lmsList[4][1], lmsList[4][2]
        x2, y2 = lmsList[8][1], lmsList[8][2]
        
        pointA = x1, y1
        pointB = x2, y2

        # Drawing circle on thumb and index finger
        cv.circle(img, pointA, 10, (255, 0, 0), -1)
        cv.circle(img, pointB, 10, (255, 0, 0), -1)

        # Drawing line between them
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Calculating the distance between pointA and pointB
        lenght = math.hypot(x1 - x2, y1 - y2)

        if lenght > 300:
            lenght = 300

        lenght_percentage = int(lenght/300 * 100) # Converting distance into percentage

        if platform.system() == 'Windows': # Checks the platform
            call(["amixer", "-D", "pulse", "sset", "Master", f"{lenght_percentage}%"])
        else:
            osascript.run(f"set volume output volume {lenght_percentage}") # Setting master volume to lenght_percentage

    # Calculating fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Displaying fps
    cv.putText(img, f"Fps: {int(fps)}", (10, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    cv.imshow("Video", img)
    key = cv.waitKey(1)

    if key==27:
        break # If key is pressed, break loop

capture.release()
cv.destroyAllWindows()

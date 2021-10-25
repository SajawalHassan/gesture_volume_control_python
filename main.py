import cv2 as cv
import time
import draw

import hand_detector_module as hand_detector
from ip import ip

address = ip
pTime = 0
detector = hand_detector.HandDetector()
drawer = draw.Draw()

# Capturing vid
capture = cv.VideoCapture()
capture.open(address)

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
        drawer.getCoordinates(img, 4, 8)
        drawer.drawLines(img)
        drawer.calculateDistance(img)

    # Calculating fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Displaying fps
    cv.putText(img, f"Fps: {int(fps)}", (10, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

    cv.imshow("Video", img)
    key = cv.waitKey(1)

    if key==27:
        break # If key is pressed, break loop

capture.release()
cv.destroyAllWindows()
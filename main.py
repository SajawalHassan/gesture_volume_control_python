import cv2 as cv
import mediapipe as mp
import time
import hand_detector_module as hand_detector

# Capturing vid (change filename to 0 if need webcam)
capture = cv.VideoCapture("videos/hand_vid_test.3gp")

pTime = 0

while True:
    # Reading currunt img
    success, img = capture.read()

    # If can't read currunt img, break loop
    if not success:
          break

    # Calculating fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Displaying fps
    cv.putText(img, f"Fps: {int(fps)}", (10, 50), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    cv.imshow("Video", img)
    key = cv.waitKey(10)

    if key==27:
        break # If key is pressed, break loop

capture.release()
cv.destroyAllWindows()

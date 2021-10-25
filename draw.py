import cv2 as cv
import math
from subprocess import call
import platform
import osascript
import hand_detector_module as hdm

class Draw():
    def getCoordinates(self, img, coor1=True, coor2=True, coor3=True, coor4=True, coor5=True):
        detector = hdm.HandDetector()

        # Detecting hand
        detector.detectHands(img, draw=False)

        # Getting positions of landmarks in detected hand
        handLmsList = detector.findPos(img, draw=False)

        if len(handLmsList) != 0:
            # Getting coordinates of hand
            if coor1:
                self.x1, self.y1 = handLmsList[coor1][1], handLmsList[coor1][2]
            else:
                pass

            if coor2:
                self.x2, self.y2 = handLmsList[coor2][1], handLmsList[coor2][2]
            else:
                pass

            if coor3:
                self.x3, self.y3 = handLmsList[coor3][1], handLmsList[coor3][2]
            else:
                pass
            
            if coor4:
                self.x4, self.y4 = handLmsList[coor4][1], handLmsList[coor4][2]
            else:
                pass
            
            if coor5:
                self.x5, self.y5 = handLmsList[coor5][1], handLmsList[coor5][2]
            else:
                pass

            self.volumePointX, self.volumePointY = handLmsList[0][1], handLmsList[0][2]

            # Sorting coordinates of hand
            self.hand_thumb = self.x1, self.y1
            self.hand_fing1 = self.x2, self.y2
            self.hand_fing2 = self.x3, self.y3
            self.hand_fing3 = self.x4, self.y4
            self.hand_fing4 = self.x5, self.y5
            self.wrist = self.volumePointY, self.volumePointX

    def drawLines(self, img, colorOuter=(255,0,0), colorInner=(0,0,0)):
        # Drawing circle on wanted finger
        cv.circle(img, self.hand_thumb, 10, colorOuter, -1)
        cv.circle(img, self.hand_thumb, 10, colorInner, 3)

        cv.circle(img, self.hand_fing1, 10, colorOuter, -1)
        cv.circle(img, self.hand_fing1, 10, colorInner, 3)

        cv.circle(img, self.hand_fing2, 10, colorOuter, -1)
        cv.circle(img, self.hand_fing2, 10, colorInner, 3)

        cv.circle(img, self.hand_fing3, 10, colorOuter, -1)
        cv.circle(img, self.hand_fing3, 10, colorInner, 3)

        cv.circle(img, self.hand_fing4, 10, colorOuter, -1)
        cv.circle(img, self.hand_fing4, 10, colorInner, 3)


        # Drawing line between them
        cv.line(img, (self.x1, self.y1), (self.volumePointX, self.volumePointY), colorOuter, 4)
        cv.line(img, (self.x1, self.y1), (self.volumePointX, self.volumePointY), colorInner, 2)
        
        cv.line(img, (self.x2, self.y2), (self.volumePointX, self.volumePointY), colorOuter, 4)
        cv.line(img, (self.x2, self.y2), (self.volumePointX, self.volumePointY), colorInner, 2)
        
        cv.line(img, (self.x3, self.y3), (self.volumePointX, self.volumePointY), colorOuter, 4)
        cv.line(img, (self.x3, self.y3), (self.volumePointX, self.volumePointY), colorInner, 2)
        
        cv.line(img, (self.x4, self.y4), (self.volumePointX, self.volumePointY), colorOuter, 4)
        cv.line(img, (self.x4, self.y4), (self.volumePointX, self.volumePointY), colorInner, 2)
        
        cv.line(img, (self.x5, self.y5), (self.volumePointX, self.volumePointY), colorOuter, 4)
        cv.line(img, (self.x5, self.y5), (self.volumePointX, self.volumePointY), colorInner, 2)
        

    def calculateDistance(self, img, drawPer=True):
        # Calculating the distance between pointA and pointB
        lenght = math.hypot(self.x1 - self.volumePointX, self.y1 - self.volumePointY)
        lenght = math.hypot(self.x2 - self.volumePointX, self.y2 - self.volumePointY)
        lenght = math.hypot(self.x3 - self.volumePointX, self.y3 - self.volumePointY)
        lenght = math.hypot(self.x4 - self.volumePointX, self.y4 - self.volumePointY)
        lenght = math.hypot(self.x5 - self.volumePointX, self.y5 - self.volumePointY)

        if lenght > 300:
            lenght = 300

        if drawPer:
            lenght_per = int(lenght/100 * 100) # Converting distance into percentage

        cv.putText(img, f"{int(lenght_per)}", self.wrist, cv.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        
        # Checks the platform
        if platform.system() == 'Linux':
            call(["amixer", "-D", "pulse", "sset", "Master", f"{lenght_per}%"])

        elif platform.system() == 'Windows':
            call(["amixer", "-D", "pulse", "sset", "Master", f"{lenght_per}%"])

        else:
            osascript.run(f"set volume output volume {lenght_per}") # Setting master volume to lenght_percentage

#! /usr/bin/env python3
import cv2
import numpy as np
from absl import app

def main(_argv):

    vid = cv2.VideoCapture(0)
    vid2 = cv2.VideoCapture(2)
    while True:
        return_value, frame = vid.read()
        return_value2, frame2 = vid2.read()
        
        cv2.imshow("Video1", frame)
        cv2.imshow("Video2", frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass

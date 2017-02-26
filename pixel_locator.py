import cv2
import os
import sys
from os.path import isfile

def locate(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.putText(param, str((x, y)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 255, 255), 1)

def main():

    path = input("Enter the path to the image: ")
    img = cv2.imread(path)
    if not isfile(path):
        print ('Invalid path.')
        sys.exit()
    cv2.namedWindow('Image')

    while True:
        cv2.setMouseCallback('Image', locate, param = img)
        cv2.imshow('Image', img)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

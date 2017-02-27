import cv2
import numpy as np

def nothing(x):
    pass

def clamp(x):
    return max(0, min(x, 255))

def main():

    print ("Press ESC to exit.")
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('Color Palette')
    cv2.createTrackbar('R', 'Color Palette', 0, 255, nothing)
    cv2.createTrackbar('G', 'Color Palette', 0, 255, nothing)
    cv2.createTrackbar('B', 'Color Palette', 0, 255, nothing)
    switch = "0 : RGB\n1 : HEX"
    cv2.createTrackbar(switch, 'Color Palette', 0, 1, nothing)

    while(1):
        cv2.imshow('Color Palette', img)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
        r = cv2.getTrackbarPos('R', 'Color Palette')
        g = cv2.getTrackbarPos('G', 'Color Palette')
        b = cv2.getTrackbarPos('B', 'Color Palette')
        s = cv2.getTrackbarPos(switch, 'Color Palette')
        img[:] = [b, g, r]
        if s == 0:
            cv2.putText(img, str((r, g, b)), (220, 256), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255-b, 255-g, 255-r), 1, lineType = cv2.LINE_AA)
        else:
            hex_code = "#{0:02x}{1:02x}{2:02x}".format(clamp(r), clamp(g), clamp(b))
            cv2.putText(img, hex_code, (220, 256), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255-b, 255-g, 255-r), 1, lineType = cv2.LINE_AA)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

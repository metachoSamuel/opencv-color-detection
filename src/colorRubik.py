#Import openCV and Numpy
import cv2
import numpy as np

#Functions
def check_color(color):
    if color == (255,0,0):
        rcolor = 'Blue'
    elif color == (0,0,255):
        rcolor = 'Red'
    elif color == (0,255,0):
        rcolor = 'Green'
    elif color == (0,255,255):
        rcolor = 'Yellow'
    elif color == (26,127,239):
        rcolor = 'Orange'

    return rcolor

def draw_contour(mask, color):
    contour,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contour:
        area = cv2.contourArea(c)
        if area > 3000 and area < 10000:
            x,y,w,h = cv2.boundingRect(c)
            color_word = check_color(color)
            cv2.rectangle(frame, (x,y), (x+w, y+h), color, 3)
            cv2.line(frame, (x,y),(x+w,y+h), color, 3)
            cv2.line(frame, (x,y), (x,y+h), color, 3)
            cv2.putText(frame, color_word, (x-10, y-10),0 ,0.75, color, 2, cv2.LINE_AA)
            
# delimit hsv color ranges
# Yellow
yellow_low = np.array([15,100,20], np.uint8)
yellow_high = np.array([45,255,255], np.uint8)

# Orange
orange_low = np.array([11,100,20], np.uint8)
orange_high = np.array([18,255,255], np.uint8)

# Blue
blue_low = np.array([80,100,20], np.uint8)
blue_high = np.array([125,255,255], np.uint8)

# Green
green_low = np.array([40,100,20], np.uint8)
green_high = np.array([70,255,255], np.uint8)

# Red
# For red, two ranges are created that will be united in a single mask
red_low_1 = np.array([0,100,20], np.uint8)
red_high_1 = np.array([12,255,255], np.uint8)

red_low_2 = np.array([165,100,20], np.uint8)
red_high_2 = np.array([179,255,255], np.uint8)

#Video Capture
video_capture = cv2.VideoCapture(1)

while True:
    # the read method returns two values, ret and frame
    ret, frame = video_capture.read()
    if ret == True:
        #convert video from bgr to hsv
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #create the masks
        yellow_mask = cv2.inRange(frameHSV, yellow_low, yellow_high)
        orange_mask = cv2.inRange(frameHSV, orange_low, orange_high)
        blue_mask = cv2.inRange(frameHSV, blue_low, blue_high)
        green_mask = cv2.inRange(frameHSV, green_low, green_high)

        # join ranges of red
        red_mask_1 = cv2.inRange(frameHSV, red_low_1, red_high_1)
        red_mask_2 = cv2.inRange(frameHSV, red_low_2, red_high_2)
        red_mask = cv2.add(red_mask_1, red_mask_2)

        # call the function draw contour
        draw_contour(yellow_mask, (0,255,255))
        draw_contour(orange_mask, (26,127,239))
        draw_contour(blue_mask, (255,0,0))
        draw_contour(green_mask, (0,255,0))
        draw_contour(red_mask, (0,0,255))

        #show video
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


video_capture.release()
cv2.destroyAllWindows()



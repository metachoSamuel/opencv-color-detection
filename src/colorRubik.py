#Import openCV and Numpy
import cv2
import numpy

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
            
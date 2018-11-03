import pprint
import imutils
from imutils import contours
from imutils.video import VideoStream
import numpy as np
import argparse
import time
import cv2

FILENAME = 'deck_1.csv'

# def raw_data_from(file_name):
#     f = open(file_name, 'r')
#     x = f.read().splitlines()
#     f.close()
#     return x
#
# def deck_from(lst):
#     return { ' '.join(a.split()[1:]) : int(a.split()[0]) for a in lst }
#
# raw_data = raw_data_from(FILENAME)
# deck = deck_from(raw_data)
# pprint.pprint(deck)

## ----------------------------------

class Rule:
    def applies(card):
        return None

    def target_bin():
        return None

## ----------------------------------

class Card:
    def color():
        return None

## ----------------------------------

cap = cv2.VideoCapture(0)

rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 21))

if (cap.isOpened()== False):
  print("Error opening video stream or file")

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame',frame)

  else:
    break

cap.release()
cv2.destroyAllWindows()

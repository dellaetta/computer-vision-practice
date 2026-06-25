import cv2
import logging
import sys

def detect_motion(img_one, img_two):
    img_diff = cv2.absdiff(img_one, img_two)
    if img_diff.max() != 0:
        print("Motion detected")
    else:
        print("No motion detected")


image_one = cv2.imread("dataset/plant_one.png")
image_two = cv2.imread("dataset/plant_two.png")

if image_one is None or image_two is None:
    logging.error(" Error loading images")
    sys.exit()

detect_motion(image_one, image_two)
detect_motion(image_one, image_one)

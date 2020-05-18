import face_recognition
import os
import cv2

KNOWN_FACES_DIR = "known_faces"
UNKNOWN_FACES_DIR = "unknown_faces"
TOLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

known_faces_arr = []
known_names_arr = []

print("loading known faces")

for name in os.listdir(KNOWN_FACES_DIR):
	for filename in os.listdir("")
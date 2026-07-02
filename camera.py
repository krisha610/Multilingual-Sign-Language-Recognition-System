import cv2


def initialize_camera():
    return cv2.VideoCapture(0)


def release_camera(camera):
    camera.release()
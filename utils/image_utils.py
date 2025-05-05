import cv2
import numpy as np

def load_image(path, size=(128, 128)):
    img = cv2.imread(path)
    img = cv2.resize(img, size)
    return img

def image_to_bytes(image):
    return image.tobytes()

def bytes_to_image(byte_data, shape):
    return np.frombuffer(byte_data, dtype=np.uint8).reshape(shape)

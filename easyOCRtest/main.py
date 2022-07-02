import os
import easyocr
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import ImageFont, ImageDraw, Image

IMAGE_PATH = 'data/dataset_img/KakaoTalk_Photo_2022-02-17-14-18-16-45.jpeg'

reader = easyocr.Reader(['ko'], gpu=False)
result = reader.readtext(IMAGE_PATH, detail=0)

print(result)


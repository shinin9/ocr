from PIL import Image
import cv2
import numpy as np
import time
import torch
import torchvision
from torch.utils.data import Dataset
from torchvision import transforms
from matplotlib import pyplot as plt
import os
import random
from tqdm import tqdm


train_path = '/home/dfx/Desktop/yujeong/Project_OCR/easyOCRtest/deep-text-recognition-benchmark/data_mnist_aug/train'
os.chdir(train_path)
train_file_list = os.listdir(train_path)

test_path = '/home/dfx/Desktop/yujeong/Project_OCR/easyOCRtest/deep-text-recognition-benchmark/data_mnist_aug/test'
os.chdir(test_path)
test_file_list = os.listdir(test_path)

val_path = '/home/dfx/Desktop/yujeong/Project_OCR/easyOCRtest/deep-text-recognition-benchmark/data_mnist_aug/val'
os.chdir(val_path)
val_file_list = os.listdir(val_path)

gt_train = open('/home/dfx/Desktop/yujeong/Project_OCR/easyOCRtest/deep-text-recognition-benchmark/data_mnist_aug/gt_train_mnist_a.txt','a')
gt_val = open('/home/dfx/Desktop/yujeong/Project_OCR/easyOCRtest/deep-text-recognition-benchmark/data_mnist_aug/gt_val_mnist_a.txt','a')
gt_test = open('/home/dfx/Desktop/yujeong/Project_OCR/easyOCRtest/deep-text-recognition-benchmark/data_mnist_aug/gt_test_mnist_a.txt','a')
gt = open('/home/dfx/Desktop/yujeong/Project_OCR/easyOCRtest/deep-text-recognition-benchmark/data_mnist_aug/mnist.txt', 'r')
lines = gt.readlines()
lines = list(set(lines))
lines = sorted(lines)

for i in tqdm(range(len(lines))):
    li = lines[i].split('\t')
    for j in range(len(train_file_list)):
        if li[0][-15:-4] in train_file_list[j]:
            gt_train.write("train/{}\t{}".format(train_file_list[j], li[1]))

    for k in range(len(test_file_list)):
        if li[0][-15:-4] in test_file_list[k]:
            gt_test.write("test/{}\t{}".format(test_file_list[k], li[1]))

    for l in range(len(val_file_list)):
        if li[0][-15:4] in val_file_list[l]:
            gt_val.write("val/{}\t{}".format(val_file_list[l], li[1]))

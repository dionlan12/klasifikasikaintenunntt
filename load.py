import os
import cv2
from PIL import Image
import numpy as np

# 
data=[]
labels=[]
# 
# ----------------
# LABELS
# Rote 0
# Sumba 1
# Sabu 2
# ----------------

# rote 0
rotes = os.listdir(os.getcwd() + "/CNN/train/rote")
for x in rotes:
    imag=cv2.imread(os.getcwd() + "/CNN/train/rote/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

# sumba 1
sumbas = os.listdir(os.getcwd() + "/CNN/train/sumba/")
for x in sumbas:
    imag=cv2.imread(os.getcwd() + "/CNN/train/sumba/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)

# sabu 2
sabus = os.listdir(os.getcwd() + "/CNN/train/sabu/")
for x in sabus:
    imag=cv2.imread(os.getcwd() + "/CNN/train/sabu/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)

tribes=np.array(data)
labels=np.array(labels)

# 
np.save("tribes",tribes)
np.save("labels",labels)
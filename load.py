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



# import os
# import cv2
# from PIL import Image
# import numpy as np

# # Inisialisasi list untuk menyimpan data gambar dan label
# data = []
# labels = []

# # Dictionary untuk menyimpan kategori dan labelnya
# category_labels = {
#     "rote": 0,
#     "sumba": 1,
#     "sabu": 2
# }

# # Fungsi untuk memuat data dari setiap kategori
# def load_data(category, label):
#     category_path = os.path.join(os.getcwd(), "cnn", "train", category)
#     images = os.listdir(category_path)
#     for image_name in images:
#         image_path = os.path.join(category_path, image_name)
#         image = cv2.imread(image_path)
#         img_from_ar = Image.fromarray(image, 'RGB')
#         resized_image = img_from_ar.resize((50, 50))
#         data.append(np.array(resized_image))
#         labels.append(label)

# # Memuat data dari setiap kategori
# for category, label in category_labels.items():
#     load_data(category, label)

# # Mengonversi list 'data' dan 'labels' ke dalam array numpy
# tribes = np.array(data)
# labels = np.array(labels)

# # Menyimpan array numpy 'data' dan 'labels' ke dalam file "tribes.npy" dan "labels.npy"
# np.save("tribes", tribes)
# np.save("labels", labels)

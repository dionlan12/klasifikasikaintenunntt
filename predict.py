

# import os
# import numpy as np
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.models import load_model

# # Baca gambar dan ubah ukurannya
# image_path = os.path.join(os.getcwd(), 'cnn/test/sumba.jpg')
# img = image.load_img(image_path, target_size=(50, 50))

# # Konversi gambar ke array numpy
# img_array = image.img_to_array(img)

# # Ekspansi dimensi untuk menyamai format input model
# test_image = np.expand_dims(img_array, axis=0)

# # Load model
# model = load_model(os.path.join(os.getcwd(), 'model.h5'))

# # Prediksi gambar
# result = model.predict(test_image)

# # Tampilkan hasil
# print(result)
# print("Result is: ", result[0][0])
# print("Prediction: " + str(np.argmax(result)))




# import os
# import cv2
# from PIL import Image
# import numpy as np
# import keras

# # Membaca gambar dari file 'sumba.jpg' menggunakan OpenCV
# imag = cv2.imread(os.getcwd() + '/cnn/test/rote_atas_3.jpg')
# # Membuat objek gambar dari array NumPy yang dibaca sebelumnya
# img_from_ar = Image.fromarray(imag, 'RGB')
# # Menyesuaikan ukuran gambar menjadi 50x50 piksel
# resized_image = img_from_ar.resize((50, 50))
# # Menambahkan dimensi batch ke gambar yang telah diubah ukurannya
# test_image = np.expand_dims(resized_image, axis=0)
# # Memuat model neural network dari file 'model.h5' menggunakan Keras
# model = keras.models.load_model(os.getcwd() + '/model.h5')
# # Melakukan prediksi menggunakan model terhadap gambar yang telah diproses
# result = model.predict(test_image)
# # Mencetak hasil prediksi
# print(result)
# # Mencetak hasil prediksi secara spesifik
# print("Result is: ", result[0][0])
# # Mencetak prediksi kelas
# print("Prediction: " + str(np.argmax(result)))


import os
import cv2
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

# Membaca gambar dari file menggunakan OpenCV
image_path = os.path.join(os.getcwd(), 'cnn', 'test', 'sumba.jpg')
imag = cv2.imread(image_path)

# Membuat objek gambar dari array NumPy yang dibaca sebelumnya
img_from_ar = Image.fromarray(imag, 'RGB')

# Menyesuaikan ukuran gambar menjadi 50x50 piksel
resized_image = img_from_ar.resize((50, 50))

# Menambahkan dimensi batch ke gambar yang telah diubah ukurannya
test_image = np.expand_dims(resized_image, axis=0)

# Memuat model neural network dari file 'model.h5'
model_path = os.path.join(os.getcwd(), 'model.h5')
model = load_model(model_path)

# Melakukan prediksi menggunakan model terhadap gambar yang telah diproses
result = model.predict(test_image)

# Mencetak hasil prediksi
print(result)
print("Result is: ", result[0][0])
print("Prediction: " + str(np.argmax(result)))



# import os
# import cv2
# from PIL import Image
# import numpy as np

# import tensorflow as tf

# imag=cv2.imread(os.getcwd() +'/cnn/test/sumba.jpg')
# img_from_ar = Image.fromarray(imag, 'RGB')
# resized_image = img_from_ar.resize((50, 50))

# test_image =np.expand_dims(resized_image, axis=0) 

# # load model
# model = tf.keras.models.load_model(os.getcwd() + '/model.h5')

# result = model.predict(test_image) 
# print(result) 
# print("Result is: ", result[0][0])
# print("Prediction: " + str(np.argmax(result)))


# import os
# import cv2
# from PIL import Image
# import numpy as np
# import tensorflow as tf

# # Membaca gambar uji
# image_path = os.path.join(os.getcwd(), 'cnn', 'test', 'rote_atas_3.jpg')
# image = cv2.imread(image_path)
# # Mengubah gambar menjadi format RGB
# image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# # Melakukan resizing gambar menjadi 50x50 piksel
# resized_image = cv2.resize(image_rgb, (50, 50))

# # Menambahkan dimensi tambahan untuk batch
# test_image = np.expand_dims(resized_image, axis=0)

# # Memuat model
# model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'model.h5'))

# # Melakukan prediksi menggunakan model
# result = model.predict(test_image)
# # Mendapatkan label kelas prediksi
# predicted_class = np.argmax(result)

# # Mencetak hasil prediksi
# print("Predicted probabilities:", result)
# print("Predicted class:", predicted_class)


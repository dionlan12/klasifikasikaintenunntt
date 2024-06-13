import os
import cv2
from PIL import Image
import numpy as np

import tensorflow as tf

imag=cv2.imread(os.getcwd() +'/cnn/test/sumba.jpg')
img_from_ar = Image.fromarray(imag, 'RGB')
resized_image = img_from_ar.resize((50, 50))

test_image =np.expand_dims(resized_image, axis=0) 

# load model
model = tf.keras.models.load_model(os.getcwd() + '/model.h5')

result = model.predict(test_image) 
print(result) 
print("Result is: ", result[0][0])
print("Prediction: " + str(np.argmax(result)))


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


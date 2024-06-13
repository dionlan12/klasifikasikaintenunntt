from flask import Flask, request, jsonify

import os
import cv2
from PIL import Image
import numpy as np
import keras

app = Flask(__name__)

application = app # our hosting requires application in passenger_wsgi

# Contoh data sementara
books = [
    {"id": 1, "title": "Python Programming"}
]

@app.route('/', methods=['GET'])
def index():
    return jsonify(books)

@app.route('/predict', methods=['GET'])
def predict():
    
    image_name = request.args.get('name')  # Mendapatkan nilai parameter 'name' dari URL
    # Membaca gambar dari file menggunakan OpenCV
    imag = cv2.imread(os.path.join(os.getcwd(), 'cnn', 'test', image_name))
    # Membuat objek gambar dari array NumPy yang dibaca sebelumnya
    img_from_ar = Image.fromarray(imag, 'RGB')
    # Menyesuaikan ukuran gambar menjadi 50x50 piksel
    resized_image = img_from_ar.resize((50, 50))
    # Menambahkan dimensi batch ke gambar yang telah diubah ukurannya
    test_image = np.expand_dims(resized_image, axis=0)
    # Memuat model neural network dari file 'model.h5' menggunakan Keras
    model = keras.models.load_model(os.path.join(os.getcwd(), 'model.h5'))
    # Melakukan prediksi menggunakan model terhadap gambar yang telah diproses
    result = model.predict(test_image)
    # Mencetak hasil prediksi
    print(result)
    # Mencetak hasil prediksi secara spesifik
    print("Result is: ", result[0][0])
    # Mencetak prediksi kelas
    print("Prediction: " + str(np.argmax(result)))

    # Dictionary untuk mapping kelas ke label
    label_mapping = {0: 'rote', 1: 'sumba', 2: 'sabu'}
    # Mendapatkan indeks kelas dengan nilai prediksi tertinggi
    predicted_class_index = np.argmax(result)

    return jsonify({"Prediction": label_mapping[predicted_class_index], "Result": result[0][0]})

if __name__ == '__main__':
    app.run(debug=True)
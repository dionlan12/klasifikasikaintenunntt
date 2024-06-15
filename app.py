from flask import Flask, request, jsonify

import os
import cv2
from PIL import Image
import numpy as np
import tensorflow as tf

import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi folder upload
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50 MB

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():

    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 415
    
    try:
        data = request.get_json()
        app.logger.debug('Request JSON: %s', data)
        
        if not data:
            return jsonify({"error": "Faileddd to decode JSON object"}), 400
        
        if 'image' not in data:
            return jsonify({"error": "No image data"}), 400
        
        # Mendapatkan string base64 dari JSON
        image_data = data['image']
        image_name = data['name']

        
        # Mendecode string base64
        image_bytes = base64.b64decode(image_data)
        
        # Nama file
        filename = secure_filename(image_name)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Menyimpan file
        with open(filepath, 'wb') as file:
            file.write(image_bytes)
        
        hasil = predict(image_name)

        return jsonify(hasil), 201

    except Exception as e:
        app.logger.error('Error: %s', str(e))
        return jsonify({"error": str(e)}), 400

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({"error": "File too large"}), 413


# Contoh data sementara
books = [
    {"id": 1, "title": "Python Programming"}
]

@app.route('/', methods=['GET'])
def index():
    return jsonify(books)



def predict(name):
     
    # image_name = request.args.get('name')  # Mendapatkan nilai parameter 'name' dari URL
    imag=cv2.imread(os.getcwd() +'/uploads/' + name)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    test_image =np.expand_dims(resized_image, axis=0) 
    model = tf.keras.models.load_model(os.getcwd() + '/model.h5')
    result = model.predict(test_image) 
    print(result) 
    print("Result is: ", result[0][0])
    print("Prediction: " + str(np.argmax(result)))

     # Dictionary untuk mapping kelas ke label
    label_mapping = {0: 'rote', 1: 'sumba', 2: 'sabu'}
    # Mendapatkan indeks kelas dengan nilai prediksi tertinggi
    predicted_class_index = np.argmax(result)

    return {"Prediction": label_mapping[predicted_class_index] }

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
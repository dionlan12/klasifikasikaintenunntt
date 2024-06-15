from flask import Flask, request, jsonify
import os
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
        iamge_name = data['name']

        
        # Mendecode string base64
        image_bytes = base64.b64decode(image_data)
        
        # Nama file
        filename = secure_filename(iamge_name)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Menyimpan file
        with open(filepath, 'wb') as file:
            file.write(image_bytes)
        
        return jsonify({"message": "File uploaded successfully", "filename": filename}), 201

    except Exception as e:
        app.logger.error('Error: %s', str(e))
        return jsonify({"error": str(e)}), 400

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({"error": "File too large"}), 413

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)









# from flask import Flask, jsonify, request
# from werkzeug.utils import secure_filename
# import os

# app = Flask(__name__)

# # Path untuk menyimpan file gambar
# app.config['UPLOAD_FOLDER'] = 'uploads'  # Menambahkan konfigurasi upload folder
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# # Data contoh
# books = {'id': 1, 'title': 'Book 1', 'author': 'Author 1', 'image': 'default.jpg'}

# # Route untuk mendapatkan semua buku
# @app.route('/books', methods=['GET'])
# def get_books():
#     return jsonify(books)

# # Route untuk mendapatkan buku berdasarkan ID
# @app.route('/books/<int:id>', methods=['GET'])
# def get_book(id):
#     book = next((book for book in books if book['id'] == id), None)
#     if book:
#         return jsonify({'book': book}), 200
#     else:
#         return jsonify({'message': 'Book not found'}), 404

# # Route untuk menambahkan buku baru
# @app.route('/books', methods=['POST'])
# def add_book():
#     if request.headers['Content-Type'] == 'application/json':
#         data = request.json
#     else:
#         data = request.form
#     new_book = {'id': int(data['id']), 'title': data['title'], 'author': data['author'], 'image': ''}
#     if 'image' in request.files:
#         file = request.files['image']
#         if file.filename != '':
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             new_book['image'] = filename
#     books.append(new_book)
#     return jsonify({'message': 'Book added'}), 201

# # Route untuk mengupdate buku
# @app.route('/books/<int:id>', methods=['PUT'])
# def update_book(id):
#     data = request.get_json()
#     book = next((book for book in books if book['id'] == id), None)
#     if book:
#         book.update(data)
#         return jsonify({'message': 'Book updated'}), 200
#     else:
#         return jsonify({'message': 'Book not found'}), 404

# # Route untuk menghapus buku
# @app.route('/books/<int:id>', methods=['DELETE'])
# def delete_book(id):
#     global books
#     books = [book for book in books if book['id'] != id]
#     return jsonify({'message': 'Book deleted'}), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)


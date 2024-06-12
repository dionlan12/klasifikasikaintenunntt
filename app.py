from flask import Flask, request, jsonify

app = Flask(__name__)

# Contoh data sementara
books = [
    {"id": 1, "title": "Python Programming", "author": "John Smith"},
    {"id": 2, "title": "Web Development with Flask", "author": "Jane Doe"}
]

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# GET single book by id
@app.route('/books/<str:name>', methods=['GET'])
def get_book(name):
    return jsonify({"message": name})

# POST a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data['title'], "author": data['author']}
    books.append(new_book)
    return jsonify(new_book), 201

# PUT update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book.update(data)
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# DELETE a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message": "Book deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)

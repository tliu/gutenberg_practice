from flask import Flask
from flask import g
from collections import Counter
import json
import nltk
import re, string
app = Flask(__name__)
books = {}

class Book:
    def __init__(self, path):
        self.path = path
        self.freq = {}

def parse_meta():
    meta = open("data/gutenberg-metadata.json")
    metadata = json.loads(meta.read())
    global books 
    books = dict([(book["Num"], Book(book["gd-path"])) for book in metadata])
    parse_freq()
    return metadata
    
def parse_freq():
    global books
    for id, book in books.items():
        if int(id) < 50:
            with open(f"data/{book.path}") as f:
                print(f'parsing {id}')
                text = f.read()
                book.freq = Counter(nltk.word_tokenize(text.lower()))


@app.route("/book/<id>")
def get_book_by_id(id):
    global books
    with open(f"data/{books[id].path}") as book:
        return book.read()

@app.route("/book/<id>/freq")
def get_book_freq(id):
    global books
    freq = books[id].freq
    return "\n".join([f"{k} {v}" for k, v in freq.items()])

@app.route("/word

if __name__ == "__main__":
    parse_meta()
    app.run()


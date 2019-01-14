from flask import Blueprint, send_from_directory, render_template
from app import app

@app.route('/', defaults={'path': ''})
@app.route("/<string:path>")
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")

@app.route('/<filename>')
def send_file(filename):
    return send_from_directory("static", filename)

@app.route('/images/<filename>')
def images_file(filename):
    return send_from_directory(app.static_folder, "images/" + filename)
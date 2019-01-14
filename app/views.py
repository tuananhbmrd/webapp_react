from flask import Blueprint, send_from_directory, render_template

web_blp = Blueprint("web", __name__)

@web_blp.route('/', defaults={'path': ''})
@web_blp.route("/<string:path>")
@web_blp.route('/<path:path>')
def index(path):
    return render_template("index.html")

@web_blp.route('/<filename>')
def send_file(filename):
    return send_from_directory("static", filename)

@web_blp.route('/images/<filename>')
def images_file(filename):
    return send_from_directory(web_blp.static_folder, "images/" + filename)
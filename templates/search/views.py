# from search.word_cloud.word_cloud import WordClouds
from templates import app
from flask import render_template, Blueprint, request, jsonify
from search.word_cloud.tokenize import Tokenize


search_blueprint = Blueprint('search',__name__)
@search_blueprint.route('/')
def index():
    return render_template("index.html", url="localhost", port="5000")


@search_blueprint.route('/result', methods=['POST', 'GET'])
def index_post():
    text = request.args.get('place', None)
    wc = Tokenize(text)
    processed_text = wc.process_text()
    return str(processed_text).replace("'", '"')

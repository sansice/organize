from search.word_cloud.word_cloud import WordClouds
from templates import app
from flask import render_template, Blueprint, request
from search.word_cloud.tokenize import Tokenize


search_blueprint = Blueprint('search',__name__)
@search_blueprint.route('/')
def index():
    return render_template("index.html", input="Amen")


@search_blueprint.route('/result', methods=['POST', 'GET'])
def index_post():
    text = request.args.get('place', None)
    wc = Tokenize(text)
    processed_text = wc.process_text()
    word_cloud = WordClouds()
    cloud = word_cloud.show_wordcloud(processed_text)
    # template = render_template("index.html", input=processed_text)
    # print(template) # TODO- Need to be fixed
    return cloud

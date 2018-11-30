from backend import is_valid_url

from models import Url

from flask import Blueprint, jsonify, request, redirect, url_for

blueprint = Blueprint('public', __name__)


@blueprint.route('/<short_url>', methods=['GET'], strict_slashes=False)
@blueprint.route('/', strict_slashes=False)
def index(short_url=None):
    """
    Routes short urls
    :param short_url: A short url string
    :return: A redirect based on the short url
    """
    if short_url:
        url_exists = Url.query.filter_by(short_url=short_url).first()
        if url_exists:
            return redirect(url_exists.url), 301
        else:
            return jsonify({
                'message': 'invalid short url'
            }), 400
    else:
        return 'Hello world!', 200


@blueprint.route('/list', strict_slashes=False)
def list_urls():
    """
    List of all the urls in the database
    :return: A HTML formatted list of urls in the database
    """
    url_list = Url.get_all_urls()
    response = '<ul>'
    for elem in url_list:
        response += '<li>id = {id} ' \
                    'url = <a href="{url}" />{url}</a> ' \
                    'short url = <a href="{short_url}">{short_url}</a></li>'.\
            format(id=elem.id, url=elem.url, short_url=request.url_root+elem.short_url)
    response += '</ul>'
    return response, 200


@blueprint.route('/shorten_url', methods=['GET', 'POST'], strict_slashes=False)
def shorten_url():

    # If method is GET, redirect to the index
    if request.method == 'GET':
        return redirect(url_for('public.index')), 301

    json_data = request.json

    if not json_data:
        return jsonify({
            'message': 'invalid JSON data received'
        }), 400

    if 'url' not in json_data:
        return jsonify({
            'message': 'url is missing from JSON POST data'
        }), 400

    url = request.json['url']

    # If the url doesn't start with http or https, append http at the beginning
    if (not url.startswith('http://')) and (not url.startswith('https://')):
        url = 'http://{}'.format(url)

    # If the url is not valid, throw out an error
    if not is_valid_url(url):
        return jsonify({
            'message': 'the url is invalid'
        }), 400

    url_exists = Url.query.filter_by(url=url).first()

    # If the url already exists, get its short_url, if it doesn't exist add it to the database
    if url_exists:
        short_url = url_exists.short_url
    else:
        short_url = Url.add_url(url).short_url

    return jsonify({
        "shortened_url": request.url_root + short_url
    }), 201

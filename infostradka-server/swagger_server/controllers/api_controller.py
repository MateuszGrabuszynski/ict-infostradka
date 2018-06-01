import connexion
import six

from swagger_server.models.rotator import Rotator  # noqa: E501
from swagger_server import util
from swagger_server.config import MONGO_HOST, MONGO_PORT, FILES_DIR

#own
from pymongo import MongoClient
import json, base64, os
from flask import send_from_directory


def get_elements():  # noqa: E501
    """Returns json with all rotator elements

     # noqa: E501


    :rtype: List[Rotator]
    """
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.infostradka

    news = db.news.find({},{"since": 1, "until": 1, "duration": 1, "title": 1, "content": 1, "important": 1, "_id": 0})
    left = db.left.find({}, {"since": 1, "until": 1, "duration": 1, "type": 1, "content": 1, "_id": 0})
    right = db.right.find({}, {"since": 1, "until": 1, "duration": 1, "source": 1, "_id": 0})

    newsdb = []
    leftdb = []
    rightdb = []

    for d1 in news:
        newsdb.append(d1)
    for d2 in left:
        leftdb.append(d2)
    for d3 in right:
        rightdb.append(d3)

    return {"left": leftdb, "right": rightdb, "news": newsdb}


def get_screenshot():
    pass


def put_screenshot(display_id, display_name, screenshot):
    #screenshot to base64
    ssencoded = base64.b64encode(screenshot.read()).decode('ascii')

    #db handler
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.infostradka #select db infostradka

    #db upload into scrshots collection
    db.scrshots.update({"display_id": display_id}, {"display_id": display_id, "display_name": display_name, "screenshot": ssencoded}, upsert=True)
    pass

def get_file(hash):
    dir = os.path.join(os.getcwd(), FILES_DIR)
    print(dir)
    return send_from_directory(directory=dir, filename=hash, mimetype='image/jpeg')

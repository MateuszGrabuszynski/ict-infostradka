import connexion
import six

from swagger_server.models.rotator import Rotator  # noqa: E501
from swagger_server import util
from swagger_server.config import MONGO_HOST, MONGO_PORT

#own
from pymongo import MongoClient
import json
import base64


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

    #print(newsdb)

    #JSON = {"left":[{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":5,"type":"video","content":{"source":"http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4","subtitles":""}},{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":15,"type":"www","content":{"source":"http://example.org/"}},{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":15,"type":"www","content":{"source":"http://example.com/"}}],"right":[{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":5,"source":"https://c1cleantechnicacom-wpengine.netdna-ssl.com/files/2018/02/Wind-Power-Birds.jpg"}],"news":[{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":15,"title":"Aaa, kotki dwa","content":"...szarobure obydwa czy coś tam jakoś tam coś.<br><br>BARDZO DUŻO TEKSTU TUTAJ...","important":0},{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":5,"title":"News2","content":"Lill news numero due","important":1}]}
    #return {newsdb}
    return {"left": leftdb, "right": rightdb, "news": newsdb}


def get_screenshot():
    pass


def put_screenshot(display_id, display_name, screenshot):
    #screenshot to base64
#    if (type(screenshot) is FileStorage):
#    print(screenshot.read())
    ssencoded = base64.b64encode(screenshot.read()).decode('ascii')

    #db handler
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client.infostradka #select db infostradka

#    print(display_id)
#    print(display_name)
#    print(ssencoded)

    #db upload into scrshots collection
    db.scrshots.insert_one({"display_id": display_id, "display_name": display_name, "screenshot": ssencoded})

    pass

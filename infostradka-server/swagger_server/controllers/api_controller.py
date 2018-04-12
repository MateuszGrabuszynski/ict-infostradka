import connexion
import six

from swagger_server.models.rotator import Rotator  # noqa: E501
from swagger_server import util


def get_elements():  # noqa: E501
    """Returns json with all rotator elements

     # noqa: E501


    :rtype: List[Rotator]
    """
    JSON = "{'left':[{'since': '2018-04-10 22:00','until': '2019-04-10 22:00','duration': 5,'type': 'video','content': {'source': 'http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4','subtitles':''}},{'since': '2018-04-10 22:00','until': '2019-04-10 22:00', 'duration': 15,'type': 'html','content': {'source': 'http://piotr.grabuszynski.com/'}}],'right':[{'since': '2018-04-10 22:00','until': '2019-04-10 22:00','duration': 5,'source': 'https://c1cleantechnicacom-wpengine.netdna-ssl.com/files/2018/02/Wind-Power-Birds.jpg'}],'news':[{'since': '2018-04-10 22:00','until': '2019-04-10 22:00','duration': 15,'title': 'Aaa, kotki dwa','content': '...szarobure obydwa czy coś tam jakoś tam coś.'},{'since': '2018-04-10 22:00','until': '2019-04-10 22:00','duration': 5,'title': 'News2','content': 'Lill news numero due'}]}"
    return JSON

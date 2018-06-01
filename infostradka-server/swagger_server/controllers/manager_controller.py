import connexion
import six

from swagger_server.models.rotator import Rotator  # noqa: E501
from swagger_server import util

#own
from flask import render_template


def get_manager():  # noqa: E501
    """Returns display

     # noqa: E501


    :rtype: List[Rotator]
    """
    return render_template("manager.html")


def get_displays_list():
    pass


def get_displays_content():
    return render_template("main_content.html", elements=[{"address": "http://xxx.pl", "period": "5"}, {"address": "http://wp.pl", "type": "file", "file": "1234"},
                                                          {"address": "http://onet.pl"}],
                           files=[{"hash": "xxx", "name": "nobody likes me :(.jpg"}, {"hash": "1234", "name": "wybrany pliczek.png"}])


def update_displays_content():
    pass


def get_right_content():
    pass


def update_right_content():
    pass


def get_news_bar():
    pass


def update_news_bar():
    pass
import connexion
import six

from swagger_server.models.rotator import Rotator  # noqa: E501
from swagger_server import util

#own
from flask import render_template


def get_display():  # noqa: E501
    """Returns display page

     # noqa: E501


    :rtype: List[Rotator]
    """
    return render_template("display.html")

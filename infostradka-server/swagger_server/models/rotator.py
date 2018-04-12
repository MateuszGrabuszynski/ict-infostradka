# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.left_element import LeftElement  # noqa: F401,E501
from swagger_server.models.news_element import NewsElement  # noqa: F401,E501
from swagger_server.models.right_element import RightElement  # noqa: F401,E501
from swagger_server import util


class Rotator(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, left: List[LeftElement]=None, right: List[RightElement]=None, news: List[NewsElement]=None):  # noqa: E501
        """Rotator - a model defined in Swagger

        :param left: The left of this Rotator.  # noqa: E501
        :type left: List[LeftElement]
        :param right: The right of this Rotator.  # noqa: E501
        :type right: List[RightElement]
        :param news: The news of this Rotator.  # noqa: E501
        :type news: List[NewsElement]
        """
        self.swagger_types = {
            'left': List[LeftElement],
            'right': List[RightElement],
            'news': List[NewsElement]
        }

        self.attribute_map = {
            'left': 'left',
            'right': 'right',
            'news': 'news'
        }

        self._left = left
        self._right = right
        self._news = news

    @classmethod
    def from_dict(cls, dikt) -> 'Rotator':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Rotator of this Rotator.  # noqa: E501
        :rtype: Rotator
        """
        return util.deserialize_model(dikt, cls)

    @property
    def left(self) -> List[LeftElement]:
        """Gets the left of this Rotator.


        :return: The left of this Rotator.
        :rtype: List[LeftElement]
        """
        return self._left

    @left.setter
    def left(self, left: List[LeftElement]):
        """Sets the left of this Rotator.


        :param left: The left of this Rotator.
        :type left: List[LeftElement]
        """

        self._left = left

    @property
    def right(self) -> List[RightElement]:
        """Gets the right of this Rotator.


        :return: The right of this Rotator.
        :rtype: List[RightElement]
        """
        return self._right

    @right.setter
    def right(self, right: List[RightElement]):
        """Sets the right of this Rotator.


        :param right: The right of this Rotator.
        :type right: List[RightElement]
        """

        self._right = right

    @property
    def news(self) -> List[NewsElement]:
        """Gets the news of this Rotator.


        :return: The news of this Rotator.
        :rtype: List[NewsElement]
        """
        return self._news

    @news.setter
    def news(self, news: List[NewsElement]):
        """Sets the news of this Rotator.


        :param news: The news of this Rotator.
        :type news: List[NewsElement]
        """

        self._news = news
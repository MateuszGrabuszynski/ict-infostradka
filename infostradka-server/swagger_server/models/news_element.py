# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class NewsElement(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, since: int=None, until: date=None, duration: int=None, title: str=None, content: str=None):  # noqa: E501
        """NewsElement - a model defined in Swagger

        :param since: The since of this NewsElement.  # noqa: E501
        :type since: int
        :param until: The until of this NewsElement.  # noqa: E501
        :type until: date
        :param duration: The duration of this NewsElement.  # noqa: E501
        :type duration: int
        :param title: The title of this NewsElement.  # noqa: E501
        :type title: str
        :param content: The content of this NewsElement.  # noqa: E501
        :type content: str
        """
        self.swagger_types = {
            'since': int,
            'until': date,
            'duration': int,
            'title': str,
            'content': str
        }

        self.attribute_map = {
            'since': 'since',
            'until': 'until',
            'duration': 'duration',
            'title': 'title',
            'content': 'content'
        }

        self._since = since
        self._until = until
        self._duration = duration
        self._title = title
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'NewsElement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NewsElement of this NewsElement.  # noqa: E501
        :rtype: NewsElement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def since(self) -> int:
        """Gets the since of this NewsElement.


        :return: The since of this NewsElement.
        :rtype: int
        """
        return self._since

    @since.setter
    def since(self, since: int):
        """Sets the since of this NewsElement.


        :param since: The since of this NewsElement.
        :type since: int
        """

        self._since = since

    @property
    def until(self) -> date:
        """Gets the until of this NewsElement.


        :return: The until of this NewsElement.
        :rtype: date
        """
        return self._until

    @until.setter
    def until(self, until: date):
        """Sets the until of this NewsElement.


        :param until: The until of this NewsElement.
        :type until: date
        """

        self._until = until

    @property
    def duration(self) -> int:
        """Gets the duration of this NewsElement.


        :return: The duration of this NewsElement.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this NewsElement.


        :param duration: The duration of this NewsElement.
        :type duration: int
        """

        self._duration = duration

    @property
    def title(self) -> str:
        """Gets the title of this NewsElement.


        :return: The title of this NewsElement.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this NewsElement.


        :param title: The title of this NewsElement.
        :type title: str
        """

        self._title = title

    @property
    def content(self) -> str:
        """Gets the content of this NewsElement.


        :return: The content of this NewsElement.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content: str):
        """Sets the content of this NewsElement.


        :param content: The content of this NewsElement.
        :type content: str
        """

        self._content = content

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.left_content import LeftContent  # noqa: F401,E501
from swagger_server import util


class LeftElement(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, since: int=None, until: date=None, duration: int=None, type: str='www', content: List[LeftContent]=None):  # noqa: E501
        """LeftElement - a model defined in Swagger

        :param since: The since of this LeftElement.  # noqa: E501
        :type since: int
        :param until: The until of this LeftElement.  # noqa: E501
        :type until: date
        :param duration: The duration of this LeftElement.  # noqa: E501
        :type duration: int
        :param type: The type of this LeftElement.  # noqa: E501
        :type type: str
        :param content: The content of this LeftElement.  # noqa: E501
        :type content: List[LeftContent]
        """
        self.swagger_types = {
            'since': int,
            'until': date,
            'duration': int,
            'type': str,
            'content': List[LeftContent]
        }

        self.attribute_map = {
            'since': 'since',
            'until': 'until',
            'duration': 'duration',
            'type': 'type',
            'content': 'content'
        }

        self._since = since
        self._until = until
        self._duration = duration
        self._type = type
        self._content = content

    @classmethod
    def from_dict(cls, dikt) -> 'LeftElement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LeftElement of this LeftElement.  # noqa: E501
        :rtype: LeftElement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def since(self) -> int:
        """Gets the since of this LeftElement.


        :return: The since of this LeftElement.
        :rtype: int
        """
        return self._since

    @since.setter
    def since(self, since: int):
        """Sets the since of this LeftElement.


        :param since: The since of this LeftElement.
        :type since: int
        """

        self._since = since

    @property
    def until(self) -> date:
        """Gets the until of this LeftElement.


        :return: The until of this LeftElement.
        :rtype: date
        """
        return self._until

    @until.setter
    def until(self, until: date):
        """Sets the until of this LeftElement.


        :param until: The until of this LeftElement.
        :type until: date
        """

        self._until = until

    @property
    def duration(self) -> int:
        """Gets the duration of this LeftElement.


        :return: The duration of this LeftElement.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this LeftElement.


        :param duration: The duration of this LeftElement.
        :type duration: int
        """

        self._duration = duration

    @property
    def type(self) -> str:
        """Gets the type of this LeftElement.


        :return: The type of this LeftElement.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this LeftElement.


        :param type: The type of this LeftElement.
        :type type: str
        """
        allowed_values = ["image", "html", "www", "video", "stream"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def content(self) -> List[LeftContent]:
        """Gets the content of this LeftElement.


        :return: The content of this LeftElement.
        :rtype: List[LeftContent]
        """
        return self._content

    @content.setter
    def content(self, content: List[LeftContent]):
        """Sets the content of this LeftElement.


        :param content: The content of this LeftElement.
        :type content: List[LeftContent]
        """

        self._content = content

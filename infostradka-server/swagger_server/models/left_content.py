# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LeftContent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, source: str=None, subtitles: str=None):  # noqa: E501
        """LeftContent - a model defined in Swagger

        :param source: The source of this LeftContent.  # noqa: E501
        :type source: str
        :param subtitles: The subtitles of this LeftContent.  # noqa: E501
        :type subtitles: str
        """
        self.swagger_types = {
            'source': str,
            'subtitles': str
        }

        self.attribute_map = {
            'source': 'source',
            'subtitles': 'subtitles'
        }

        self._source = source
        self._subtitles = subtitles

    @classmethod
    def from_dict(cls, dikt) -> 'LeftContent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LeftContent of this LeftContent.  # noqa: E501
        :rtype: LeftContent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source(self) -> str:
        """Gets the source of this LeftContent.


        :return: The source of this LeftContent.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this LeftContent.


        :param source: The source of this LeftContent.
        :type source: str
        """

        self._source = source

    @property
    def subtitles(self) -> str:
        """Gets the subtitles of this LeftContent.


        :return: The subtitles of this LeftContent.
        :rtype: str
        """
        return self._subtitles

    @subtitles.setter
    def subtitles(self, subtitles: str):
        """Sets the subtitles of this LeftContent.


        :param subtitles: The subtitles of this LeftContent.
        :type subtitles: str
        """

        self._subtitles = subtitles

# coding: utf-8

from __future__ import absolute_import

from typing import List

from querying.neo4j_query.lib.model.base_model_ import Model
from querying.neo4j_query.lib.model.edge import Edge


class Graph(Model):
    def __init__(self, id: str = None, label: str = None, directed: bool = True, type: str = None,
                 metadata: object = None, nodes: dict = None, edges: List[Edge] = None):
        self._id = id
        self._label = label
        self._directed = directed
        self._type = type
        self._metadata = metadata
        self._nodes = nodes
        self._edges = edges

        self.types = {
            'id': str,
            'label': str,
            'directed': bool,
            'type': str,
            'metadata': object,
            'nodes': dict,
            'edges': List[Edge]
        }

    @property
    def id(self) -> str:
        """Gets the id of this Graph.


        :return: The id of this Graph.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Graph.


        :param id: The id of this Graph.
        :type id: str
        """

        self._id = id

    @property
    def label(self) -> str:
        """Gets the label of this Graph.


        :return: The label of this Graph.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this Graph.


        :param label: The label of this Graph.
        :type label: str
        """

        self._label = label

    @property
    def directed(self) -> bool:
        """Gets the directed of this Graph.


        :return: The directed of this Graph.
        :rtype: bool
        """
        return self._directed

    @directed.setter
    def directed(self, directed: bool):
        """Sets the directed of this Graph.


        :param directed: The directed of this Graph.
        :type directed: bool
        """

        self._directed = directed

    @property
    def type(self) -> str:
        """Gets the type of this Graph.


        :return: The type of this Graph.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Graph.


        :param type: The type of this Graph.
        :type type: str
        """

        self._type = type

    @property
    def metadata(self) -> object:
        """Gets the metadata of this Graph.


        :return: The metadata of this Graph.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: object):
        """Sets the metadata of this Graph.


        :param metadata: The metadata of this Graph.
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def nodes(self) -> dict:
        """Gets the nodes of this Graph.


        :return: The nodes of this Graph.
        :rtype: GraphFormatNode
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes: dict):
        """Sets the nodes of this Graph.


        :param nodes: The nodes of this Graph.
        :type nodes: GraphFormatNode
        """

        self._nodes = nodes

    @property
    def edges(self) -> List[Edge]:
        """Gets the edges of this Graph.


        :return: The edges of this Graph.
        :rtype: List[Edge]
        """
        return self._edges

    @edges.setter
    def edges(self, edges: List[Edge]):
        """Sets the edges of this Graph.


        :param edges: The edges of this Graph.
        :type edges: List[Edge]
        """

        self._edges = edges

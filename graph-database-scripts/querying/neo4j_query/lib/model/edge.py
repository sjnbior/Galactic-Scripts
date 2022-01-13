# coding: utf-8

from __future__ import absolute_import

from querying.neo4j_query.lib.model.base_model_ import Model


class Edge(Model):
    def __init__(self, id: str = None, source: str = None, target: str = None, relation: str = None,
                 directed: bool = True, metadata: object = None):
        self._id = id
        self._source = source
        self._target = target
        self._relation = relation
        self._directed = directed
        self._metadata = metadata

        self.types = {
            'id': str,
            'source': str,
            'target': str,
            'relation': str,
            'directed': bool,
            'metadata': object
        }

    def todict(self):
        return {
            "id": self._id,
            "source": self._source,
            "target": self._target,
            "relation": self._relation,
            "directed": self._directed
        }

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False

        return self._id == other._id

    @property
    def id(self) -> str:
        """Gets the id of this GraphFormatEdge.


        :return: The id of this GraphFormatEdge.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this GraphFormatEdge.


        :param id: The id of this GraphFormatEdge.
        :type id: str
        """

        self._id = id

    @property
    def source(self) -> str:
        """Gets the source of this GraphFormatEdge.


        :return: The source of this GraphFormatEdge.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this GraphFormatEdge.


        :param source: The source of this GraphFormatEdge.
        :type source: str
        """

        self._source = source

    @property
    def target(self) -> str:
        """Gets the target of this GraphFormatEdge.


        :return: The target of this GraphFormatEdge.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target: str):
        """Sets the target of this GraphFormatEdge.


        :param target: The target of this GraphFormatEdge.
        :type target: str
        """

        self._target = target

    @property
    def relation(self) -> str:
        """Gets the relation of this GraphFormatEdge.


        :return: The relation of this GraphFormatEdge.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation: str):
        """Sets the relation of this GraphFormatEdge.


        :param relation: The relation of this GraphFormatEdge.
        :type relation: str
        """

        self._relation = relation

    @property
    def directed(self) -> bool:
        """Gets the directed of this GraphFormatEdge.


        :return: The directed of this GraphFormatEdge.
        :rtype: bool
        """
        return self._directed

    @directed.setter
    def directed(self, directed: bool):
        """Sets the directed of this GraphFormatEdge.


        :param directed: The directed of this GraphFormatEdge.
        :type directed: bool
        """

        self._directed = directed

    @property
    def metadata(self) -> object:
        """Gets the metadata of this GraphFormatEdge.


        :return: The metadata of this GraphFormatEdge.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata: object):
        """Sets the metadata of this GraphFormatEdge.


        :param metadata: The metadata of this GraphFormatEdge.
        :type metadata: object
        """

        self._metadata = metadata

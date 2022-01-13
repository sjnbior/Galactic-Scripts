import math

import networkx as nx
from networkx import DiGraph

from querying.neo4j_query.lib.model.graph import Graph


class GraphReconstructor:
    """object that reconstructs a nx_graph in memory from a Causal Flow nx_graph"""

    def __init__(self, api_graph: Graph):
        self._api_graph = api_graph
        self._nx_graph = self._reconstruct_graph(api_graph)
        self._is_cyclic = None

    @property
    def nx_graph(self):
        return self._nx_graph

    @property
    def api_graph(self):
        return self._api_graph

    @property
    def is_cyclic(self):
        if self._is_cyclic is None:
            self._is_cyclic = len(list(nx.simple_cycles(self.nx_graph))) > 0
        return self._is_cyclic

    def _reconstruct_graph(self, api_graph: Graph):
        self._nodes = api_graph.nodes
        self._edges = api_graph.edges

        # reconstruct the nx_graph in memory
        g = DiGraph()

        # add nodes
        print(self._nodes.items())
        for k, v in self._nodes.items():
            # reconstruct the node with relevant metadata
            g.add_nodes_from([
                (
                    v["label"],
                    v["metadata"]
                )
            ])

        # link nodes up with edges
        for e in self._edges:
            metadata = e.metadata
            metadata["inverseLogConfidenceScore"] = round(-math.log(1 - metadata["confidenceScore"], 2), 2)
            source_label = self._nodes[e.source]["label"]
            target_label = self._nodes[e.target]["label"]
            # reconstruct the edge with relevant metadata
            g.add_edges_from([
                (
                    source_label, target_label, metadata
                )
            ])

        # we've reconstructed the nx_graph
        return g

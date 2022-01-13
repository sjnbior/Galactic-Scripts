import uuid
from typing import List

import networkx as nx
from neo4j import Record
from neo4j.graph import Node, Relationship

from querying.neo4j_query.lib.model.edge import Edge
from querying.neo4j_query.lib.model.graph import Graph
from querying.neo4j_query.lib.model.graph_reconstructor import GraphReconstructor


def convert_response_to_paths(records: List[Record]) -> dict:
    result_paths = []
    result_nodes = {}
    for record in records:
        path_edges = []
        record_edges = record["edges"]
        for r_edge in record_edges:
            edge = record_edge_to_api_edge(r_edge)
            path_edges.append(edge)

        result_paths.append(path_edges)

        record_nodes = record["nodes"]
        [result_nodes.update(record_node_to_dict(record_node)) for record_node in record_nodes]

    return {"paths": result_paths, "nodes": result_nodes}


def deconstruct_paths(paths_with_nodes: dict) -> Graph:
    paths = paths_with_nodes["paths"]
    edges_in_one_list = []
    for p in paths:
        edges_in_one_list.extend(p)

    unique_edges = set(edges_in_one_list)

    nodes = paths_with_nodes["nodes"]

    return Graph(id=str(uuid.uuid4()), label="Interaction Graph", type="paths", metadata={}, nodes=nodes,
                 edges=list(unique_edges))


def convert_records_to_graphs(records: List[Record]) -> List[Graph]:
    ret = []
    for record in records:
        if len(record["entities"]) > 0:
            ret.append(record_to_graph(record))
    return ret


def record_to_graph(record: Record) -> Graph:
    record_nodes = record["entities"]
    record_edges = record["interactions"]

    nodes = {}
    [nodes.update(record_node_to_dict(record_node)) for record_node in record_nodes]

    edges = [record_edge_to_api_edge(record_edge) for record_edge in record_edges]

    return Graph(id=str(uuid.uuid4()), label="Interaction Graph", type="paths", metadata={}, nodes=nodes, edges=edges)


def record_node_to_dict(record_node: Node) -> dict:
    node_dict = {str(record_node.id): {
        "metadata": {},
        "label": record_node["name"]
    }}
    node_dict[str(record_node.id)]["metadata"].update(record_node)

    return node_dict


def record_edge_to_api_edge(record_edge: Relationship) -> Edge:
    edge_id = str(record_edge.id)
    start_node_id = str(record_edge.start_node.id)
    end_node_id = str(record_edge.end_node.id)
    relation = record_edge.type
    metadata = {}
    metadata.update(record_edge)

    return Edge(id=edge_id, source=start_node_id, target=end_node_id, relation=relation, metadata=metadata)


def clean_of_empty_strings(iterator):
    while "" in iterator:
        iterator.remove("")
    return iterator


def get_gml_from_graph(graph: Graph) -> str:
    reconstructedGraph = GraphReconstructor(graph).nx_graph
    gml_str = "\n".join(nx.generate_gml(reconstructedGraph))
    return gml_str

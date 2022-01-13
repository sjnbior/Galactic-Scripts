# Neo4j Query in Python

## Overview

This tool is meant to return Neo4j query results in [GML](https://en.wikipedia.org/wiki/Graph_Modelling_Language)
or [JGF](https://jsongraphformat.info/). GML can be exported to Cytoscape.

## Requirements

Python 3.5+

## Usage

To run the tool, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m neo4j_query -h
```

## Queries

The query to run on the Neo4j graph has a single requirement:
It must return nodes and edges.

Example contents of query.txt:

```
MATCH (source:Entity), (target:Entity)
WHERE (source.id in ["HGNC:17868"]) AND (target.id in ["HGNC:9108"])
CALL apoc.algo.allSimplePaths(source, target, 'INTERACTS>', 2)
YIELD path
UNWIND relationships(path) AS r
RETURN relationships(path) as edges, nodes(path) as nodes, MIN(r.confidenceScore) AS min_confidence, length(path) as length
ORDER BY length, min_confidence DESC
LIMIT 50
```

Notice the "as nodes" and "as edges" expressions. Returning these is mandatory for the tool to generate GML and JGF from
the query.

## Credentials

All neo4j databases must be accessed through a **URI**, and can only be accessed with a **username** and **password**.
This is what the credentials file is for.

Example contents of credentials.json:

```json
{
  "uri": "bolt://localhost:7687",
  "username": "neo4j",
  "password": "1234"
}
```


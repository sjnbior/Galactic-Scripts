# Galactic Data Scripts

Welcome to the Galactic Data Scripts repository.

This is a collection of scripts that Galactic Data customers may find useful.

## Getting started

Please feel free to clone this repository to run the scripts locally.

## Support

If you get stuck or require assistance running any of the scripts, please do not hesitate to reach out to info@biorelate.com. You can also post feedback to feedback@biorelate.com

## Description

## data-download-scripts

### [download_via_signed_urls.sh](./data-download-scripts/download_via_signed_urls.sh)

A simple shell script to enable multiple simultaneous download of all of Galactic Data (requires manually adding the signed urls from the release email).

## graph-database-scripts

### [processing](./graph-database-scripts/processing)

A Python 3.5+ tool intended to get only the unique entities from the aggregate table in Galactic Data. This is useful in preparation to upload concepts as nodes in a graph database.

### [querying](./graph-database-scripts/querying)

A Python 3.5+ tool intended to return Neo4j query results in [GML](https://en.wikipedia.org/wiki/Graph_Modelling_Language) or [JGF](https://jsongraphformat.info/). GML can be exported to Cytoscape.

## Uploading Galactic Data to Neo4j
### Preparing the Data

We need to generate `entities.csv` using `aggregate.csv` and [get_unique_entities.py](./graph-database-scripts/processing/get_unique_entities.py).

```bash
pip3 install -r graph-database-scripts/processing/requirements.txt 
```
```bash
cd graph-database-scripts/processing
```
```bash
python3 get_unique_entities.py -i path/to/aggregate.csv -o path/to/entities.csv
```

We use `aggregate.csv` and `entities.csv` to load the interactions in a graph database. 
We do this with [LOAD CSV](https://neo4j.com/docs/cypher-manual/current/clauses/load-csv/) in the following Cypher scripts run separately.

### Loading Nodes (Entities)
```roomsql
LOAD CSV WITH HEADERS FROM 'file:///entities.csv' AS row
CREATE (e:Entity {_id:row.id, name:row.name, type:row.type})
RETURN count(e);

CREATE INDEX FOR (e:Entity) ON (e._id);
```
### Loading Edges (Interactions)
```roomsql
:auto USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM 'file:///aggregate.csv' AS row
MATCH (e1:Entity {_id: row.Cause_ID})
MATCH (e2:Entity {_id: row.Effect_ID})
CREATE (e1)-[:INTERACTS {
    _id:toInteger(row.Interaction_ID),
    confidenceScore:toFloat(row.Confidence_Score),
    relationshipType:row.Relationship_Type,
    relationshipProperty:row.Relationship_Property,
    totalMentions:toInteger(row.Total_Mentions),
    totalDocuments:toInteger(row.Total_Documents),
    increasesScore:toInteger(row.Increases_Score),
    status:row.Status
}]->(e2);

CREATE INDEX FOR ()-[r:INTERACTS]-() ON (r._id);
```

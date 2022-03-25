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

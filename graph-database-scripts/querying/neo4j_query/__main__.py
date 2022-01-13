import argparse
import json
import logging

from neo4j import GraphDatabase

from querying.neo4j_query.lib.processing.data_processing import convert_response_to_paths, deconstruct_paths, \
    get_gml_from_graph


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--query", required=True,
                        help="File to read the Neo4j query from")

    parser.add_argument("--gml", required=True,
                        help="The file to write the GML data to")

    parser.add_argument("--json", required=False,
                        help="The json file to write graph in Json Graph Format")

    parser.add_argument("-c", "--credentials", required=True,
                        help="Json file with the database uri, username and password")

    args = parser.parse_args(argv)

    input_file = args.query
    output_gml = args.gml
    output_json = args.json
    cred_file = args.credentials

    # credentials
    with open(cred_file, "r") as f:
        credentials = json.load(f)

    # query file
    with open(input_file, "r") as f:
        query = f.read()

    # connect to db
    uri = credentials["uri"]
    username = credentials["username"]
    password = credentials["password"]
    logging.info("Connecting to \"{}\"".format(uri))
    driver = GraphDatabase.driver(uri, auth=(username, password))

    # query neo4j
    result = []
    with driver.session() as session:
        query_result = session.run(query)
        for row in query_result:
            result.append(row)

    # disconnect from db
    driver.close()

    # create the Graph object
    paths_object = convert_response_to_paths(result)
    graph = deconstruct_paths(paths_object)

    # write as gml file
    logging.info("Writing GML to \"{}\"".format(output_gml))
    gml_string = get_gml_from_graph(graph)
    with open(output_gml, "w") as f:
        f.write(gml_string)

    # if need, write as json graph format
    if output_json is not None:
        # convert to jgf and write to json file
        logging.info("Writing JGF to \"{}\"".format(output_json))
        with open(output_json, "w") as f:
            json.dump(graph.to_dict(), f)

    return 0


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()

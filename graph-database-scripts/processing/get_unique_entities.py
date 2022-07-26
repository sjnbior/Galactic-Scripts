import argparse
import logging

import pandas as pd


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True,
                        help="The csv with aggregate interactions")
    parser.add_argument("-o", "--output", required=True,
                        help="The csv to create with the unique entities of the interactions")
    args = parser.parse_args(argv)

    input_csv = args.input
    output_csv = args.output

    logging.info("Reading interactions from \"{}\"".format(input_csv))
    df_input = pd.read_csv(input_csv)

    logging.info("Uniquefying the entities")
    entity_id_to_name = dict()
    for row in df_input.itertuples():
        entity_id_to_name[getattr(row, "Cause_ID")] = [getattr(row, "Cause_Name"), getattr(row, "Cause_Type")]
        entity_id_to_name[getattr(row, "Effect_ID")] = [getattr(row, "Effect_Name"), getattr(row, "Effect_Type")]

    entity_id_to_name_tuples = [(k, l[0], l[1]) for k, l in entity_id_to_name.items()]

    logging.info("Writing entities to \"{}\"".format(output_csv))
    df_output = pd.DataFrame(entity_id_to_name_tuples)
    df_output.columns = ["id", "name", "type"]

    df_output.to_csv(output_csv, index=False)

    return 0


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    main()

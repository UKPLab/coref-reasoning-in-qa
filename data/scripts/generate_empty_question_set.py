"""
This script is used to generate adversary dataset in which question field is set to empty based on the original dataset.
"""
import os
import gzip
import json
import shutil
import sys

if __name__ == "__main__":
    datasets = ["quoref"]
    src_folder = sys.argv[1]
    out_folder = sys.argv[2]

    f_out = open(os.path.join(out_folder, "train-bart-emptyqst.json"), "w")
    with open(os.path.join(src_folder, "train-bart.json")) as f_in:
        data = json.load(f_in)
        for paragraphs in data["data"]:
            for context in paragraphs["paragraphs"]:
                for qa in context["qas"]:
                    qa["question"] = "empty"

    json.dump(data, f_out, indent=4)
    f_out.close()

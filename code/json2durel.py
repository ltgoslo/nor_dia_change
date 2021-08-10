#! /bin/env python3
# coding: utf-8

import sys
import csv
from smart_open import open
import json
import os

jsonfile = sys.argv[1]
grouping = sys.argv[2]

with open(jsonfile, "r") as f:
    usages = json.load(f)

lemma = os.path.basename(jsonfile).split("_")[1]
pos = "NN"
date = os.path.basename(jsonfile).split("_")[0].split("-")[0]
identifier = os.path.basename(jsonfile).split(".")[0]

outfile = open(jsonfile.replace("json.", "tsv."), "a")


outfile.write(
    "lemma\tpos\tdate\tgrouping\tidentifier\tdescription\tcontext\tindexes_target_token\tindexes_target_sentence\n"
)

writer = csv.writer(outfile, delimiter="\t", quoting=csv.QUOTE_MINIMAL, dialect="unix")

for sentence in usages:
    description = ""
    context = sentence[1]
    target = context.find(lemma)
    if target != -1:
        indexes_target_token = f"{target}:{target+len(lemma)}"
    else:
        target = "0:0"
    indexes_target_sentence = f"0:{len(context)}"
    writer.writerow(
        [
            lemma,
            pos,
            date,
            grouping,
            identifier,
            description,
            context,
            indexes_target_token,
            indexes_target_sentence,
        ]
    )

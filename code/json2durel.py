#! /bin/env python3
# coding: utf-8

import sys
import csv
from smart_open import open
import json
import os
from nltk.tokenize import wordpunct_tokenize
from leven import levenshtein

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

seen = set()
discarded_count = 0

for sentence in usages:
    description = ""
    context = sentence[1].strip()
    if context in seen:
        discarded_count += 1
        continue
    seen.add(context)
    tokenized_context = wordpunct_tokenize(context)
    # First we are looking for the 100% match:
    target_token = None
    for token in tokenized_context:
        if token == lemma:
            target_token = token
    # if no 100% match is found, let's look for similar words:
    if not target_token:
        current_candidate = (None, 100)
        for token in tokenized_context:
            # We are interested only in tokens starting with the same character as lemma
            if token[0] != lemma[0]:
                continue
            distance = levenshtein(token, lemma)
            if distance < current_candidate[1]:
                current_candidate = (token, distance)
        target_token = current_candidate[0]

    if target_token:
        target = context.find(target_token)
        indexes_target_token = f"{target}:{target + len(target_token)}"
    else:
        indexes_target_token = "0:0"
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

if discarded_count:
    print(f"{discarded_count} duplicates discarded", file=sys.stderr)

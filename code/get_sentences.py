#! /bin/env python3
# coding: utf-8

import sys
import pandas as pd
from smart_open import open
import json
from langdetect import detect

targetlistfile = sys.argv[1]
corpusfile = sys.argv[2]
identifier = sys.argv[3]

targets = {}

for line in open(targetlistfile, "r"):
    word = line.strip().split("\t")[0]
    targets[word.strip() + "_NOUN"] = []

print(f"{len(targets)} target words to extract", file=sys.stderr)

corpus = pd.read_csv(corpusfile, index_col="ID")

for idx, lemmas, raw in corpus[["LEMMAS", "RAW"]].itertuples():
    text = raw.strip()
    try:
        language = detect(text)
    except:
        continue
    if language != "no":
        continue
    split_lemmas = lemmas.split()
    bag_of_lemmas = set([w for w in split_lemmas])
    for target in targets:
        if target in bag_of_lemmas:
            targets[target].append([split_lemmas, text])

for target in targets:
    print(f"{target}: {len(targets[target])} examples found", file=sys.stderr)
    outfilename = f"{identifier}_{target}.json.gz"
    with open(outfilename, "w") as f:
        out = json.dumps(targets[target], ensure_ascii=False, indent=4)
        f.write(out)

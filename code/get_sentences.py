#! /bin/env python3
# coding: utf-8

import sys
import pandas as pd
from smart_open import open

targetlistfile = sys.argv[1]
corpusfile = sys.argv[2]

targets = {}

for line in open(targetlistfile, "r"):
    word, senses, period = line.strip().split("\t")
    targets[word.strip() + "_NOUN"] = []

print(f"{len(targets)} target words to extract", file=sys.stderr)

corpus = pd.read_csv(corpusfile, index_col="ID")

for idx, lemmas, raw in corpus[["LEMMAS", "RAW"]].itertuples():
    split_lemmas = lemmas.split()
    bag_of_lemmas = set(split_lemmas)
    for target in targets:
        if target in bag_of_lemmas:
            targets[target].append([split_lemmas, raw])

for target in targets:
    print(f"{target}: {len(targets[target])} examples found", file=sys.stderr)

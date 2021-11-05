#! /bin/env python3.9
# coding: utf-8

import sys
import pandas as pd

target_word = sys.argv[1]

sentences = pd.read_csv(f"norwegian/data/{target_word}/uses.csv", sep="\t")

sentences = sentences[["identifier", "context"]]

clusters = pd.read_csv(f"norwegian/clusters/{target_word}.csv", sep="\t")

senses = sorted(set(clusters["cluster"].values))

print(target_word)
print(f"Senses: {senses}")

sentences = dict(sentences.values)
clusters = dict(clusters.values)

time_bins = sorted(set([i.split("_")[0] for i in clusters]))

for tbin in time_bins:
    print("========")
    print(tbin)
    print("========")
    for sense in senses:
        print("========")
        print(f"Sense {sense}:")
        print("========")
        counter = 1
        for identifier in clusters:
            if identifier.startswith(tbin) and clusters[identifier] == sense:
                print(f"{counter}\t{sentences[identifier]}")
                counter += 1





#! /bin/env python3
# coding: utf-8

import sys
import pandas as pd
from smart_open import open
import json
from os import path
from scipy.stats import spearmanr


def ipm(count, size):
    return count / size * 1000000


if __name__ == '__main__':

    # For Subset 1:
    # time0 = "1929-1965"
    # time1 = "1970-2015"
    # time0_size = 57000000
    # time1_size = 175000000

    # For subset 2:
    time0 = "1980-1990"
    time1 = "2012-2019"
    time0_size = 43000000
    time1_size = 649000000

    dataset = sys.argv[1]  # Annotated dataset
    jsons = sys.argv[2]  # Raw JSONs directory

    annotated = pd.read_csv(dataset, delimiter="\t")
    words = annotated["lemma"].values
    graded = annotated["change_graded"].values

    print(f"{len(words)} words loaded from the annotated dataset")

    usages = {w: None for w in words}
    for word in words:
        usage0 = json.load(open(path.join(jsons, f"{time0}_{word}_NOUN.json.gz")))
        usage1 = json.load(open(path.join(jsons, f"{time1}_{word}_NOUN.json.gz")))
        usages[word] = [len(usage0), len(usage1)]
    assert len(words) == len(usages)

    print(usages)
    freq_deltas = [ipm(usages[word][1], time1_size) - ipm(usages[word][0], time0_size)
                   for word in words]
    print(freq_deltas)

    print("Spearman rank correlation between frequency differences (IPM) and change scores:")
    print(spearmanr(graded, freq_deltas))

#! /bin/env/ python3
# coding: utf-8

from smart_open import open
from scipy.stats import percentileofscore
import random
import numpy as np
import sys


def get_freqdict(wordlist, vocablist, corpus_size, shared_voc, return_percentiles=True):
    all_freqs = []
    word_freq = {}
    for word in wordlist:
        counts = [vocab[word] for vocab in vocablist]
        frequency = [counts[i] / corpus_size[i] for i in range(len(vocablist))]
        # mean_frequency = sum(frequency) / len(frequency)
        # print(mean_frequency)
        word_freq[word] = frequency

    for word in shared_voc:
        counts = [vocab[word] for vocab in vocablist]
        frequency = [counts[i] / corpus_size[i] for i in range(len(vocablist))]
        all_freqs.append(frequency)

    if return_percentiles:
        percentiles = {}
        for word in wordlist:
            percentiles[word] = [int(percentileofscore([el[i] for el in all_freqs],
                                                       word_freq[word][i]))
                                 for i in range(len(word_freq[word]))]
        return percentiles

    else:
        return word_freq


def output_results(target_dict, rest_dict, vocablist):

    finallist = set()
    missing_perc = []

    for i in target_dict:
        print("Target: ", i)
        perc = np.array(target_dict[i])
        print(perc)
        candidates = set([w for w in rest_dict
                          if np.max(np.absolute(np.array(rest_dict[w]) - perc)) < 2
                          and w not in finallist])
        if len(candidates) < 2:
            missing_perc.append(target_dict[i])
            print(f"No candidates for {i}")
            continue
        sl = random.sample(candidates, 5)
        for el in sl:
            print("\t".join([el, "0", "0", "0"]), [vocab[el] for vocab in vocablist])
            finallist.add(el)
        print("=" * 30)

    return list(finallist)


targetlistfile = sys.argv[1]
vocab0file = sys.argv[2]
vocab1file = sys.argv[3]
targets = {}

for line in open(targetlistfile, "r"):
    filler, senses, period = line.strip().split("\t")
    targets[filler.strip() + "_NOUN"] = []

print("Gold dataset length: ", len(targets))

vocab_0 = {}
vocab_1 = {}

with open(vocab0file, "r") as f:
    for line in f:
        filler, freq = line.strip().split("\t")
        vocab_0[filler] = int(freq)

with open(vocab1file, "r") as f:
    for line in f:
        filler, freq = line.strip().split("\t")
        vocab_1[filler] = int(freq)


all_vocabs = [vocab_0, vocab_1]

# Our corpora sizes:
# 1929-1965: 62354195
# 1970-2020: 195094508
# 1980-1990: 48065811
# 2012-2019: 729634768

corpus_size_0 = int(sys.argv[4])
corpus_size_1 = int(sys.argv[5])

intersec = set.intersection(*map(set, all_vocabs))

print("Generating fillers...", file=sys.stderr)
wordfreq = get_freqdict(targets, all_vocabs, [corpus_size_0, corpus_size_1], intersec)

fillers = set()
for voc_word in intersec:
    if voc_word not in targets and voc_word.endswith("_NOUN"):
        fillers.add(voc_word)

print("Frequency filtering...", file=sys.stderr)
FREQ_THRESHOLD = 10  # We do not consider fillers less frequent than this
frequent_fillers = set()
for filler in fillers:
    if vocab_0[filler] < FREQ_THRESHOLD or vocab_1[filler] < FREQ_THRESHOLD:
        continue
    else:
        frequent_fillers.add(filler)
print(f"{len(frequent_fillers)} potential fillers")
fillerfreq = get_freqdict(frequent_fillers, all_vocabs, [corpus_size_0, corpus_size_1], intersec)

print("Producing results...", file=sys.stderr)
res = output_results(wordfreq, fillerfreq, all_vocabs)

print(f"{len(res)} fillers found", file=sys.stderr)

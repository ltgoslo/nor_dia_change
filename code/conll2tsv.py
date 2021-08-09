#! python3
# coding: utf-8

import sys
from smart_open import open
from helpers import extract_proper, check_word, num_replace
import csv

SOURCE_FILE = sys.argv[1]  # Must be *.conllu.gz

TEMPFILE0_NAME = SOURCE_FILE.replace('.conllu', '.txt')

processed = extract_proper(SOURCE_FILE, TEMPFILE0_NAME)  # Can turn off sentence breaks

print('Processed %d lines' % processed, file=sys.stderr)

print('Filtering the corpus...', file=sys.stderr)

functional = set('ADP AUX CCONJ DET PART PRON SCONJ PUNCT'.split())
SKIP_1_WORD = True

corpus_file = open(TEMPFILE0_NAME, 'r')
FILTERED_CORPUS_FILE_NAME = TEMPFILE0_NAME.replace('.txt', '_contexts.tsv')
filtered = open(FILTERED_CORPUS_FILE_NAME, 'a')

filtered.write('ID,LEMMAS,RAW\n')
counter = 0
error_counter = 0

rawwriter = csv.writer(filtered, delimiter=',', quotechar='"', dialect='unix')

for line in corpus_file:
    res = line.strip().split('\t')
    try:
        (tagged, raw) = res
    except ValueError:
        error_counter += 1
        continue
    good = []
    for w in tagged.split():
        try:
            (token, pos) = w.split('_')
        except:
            token = w
            pos = "UNK"
            print(line, file=sys.stderr)
        checked_word = check_word(token, pos, nofunc=functional)   # Can feed stopwords list
        if not checked_word:
            continue
        if pos == 'NUM' and token.isdigit():  # Replacing numbers with xxxxx of the same length
            checked_word = num_replace(checked_word)
        good.append(checked_word)
    if SKIP_1_WORD:  # May be, you want to filter out one-word sentences
        if len(good) < 2:
            continue
    new_tagged = ' '.join(good)
    identifier = str(counter)
    rawwriter.writerow([identifier, new_tagged, raw])
    counter += 1

corpus_file.close()
filtered.close()
print('Erroneous lines:', error_counter, file=sys.stderr)
print('Final training corpus:', FILTERED_CORPUS_FILE_NAME, file=sys.stderr)

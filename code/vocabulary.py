#! python3

# Simple tool to extract vocabulary from the corpus

import sys
from collections import Counter

THRESHOLD = int(sys.argv[1])

words = Counter()

for line in sys.stdin:
    tokenized = line.strip()[1:-1].split()
    words.update(tokenized)

print("Vocabulary size before pruning:", len(words), file=sys.stderr)

a = words.most_common(THRESHOLD)
for w in a:
    print(f"{w[0]}\t{w[1]}")

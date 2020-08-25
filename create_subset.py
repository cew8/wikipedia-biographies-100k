import os
import json
from collections import defaultdict

indexes = (idx for idx in open('train.nb', 'r'))
sentences = (sent for sent in open('train.sent', 'r'))

articles = defaultdict(list)

for article_nr, idx in enumerate(indexes, 1):
    n_sentences = idx[:idx.find('\n')]
    for n in range(int(n_sentences)):
        articles[article_nr].append(next(sentences))
    if article_nr % 1000 == 0:
        print(f'Currently at {article_nr} articles')
    if article_nr % 100000 == 0:
        break

with open('biography_subset_100k.json', 'wt') as f:
    json.dump(articles, f)

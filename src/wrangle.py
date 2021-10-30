import jieba
import re
from utils import *
from collections import Counter
from itertools import chain

if __name__ == '__main__':
    # Split sentence into words
    data_file = "../data/takeout_comment.csv"
    splited_file = "../data/splited.csv"
    wordcnt_file = "../data/wordcnt.csv"
    comments = read_csv(data_file)
    # cut_comments = cut_sentences([c[1] for c in comments], output_file=splited_file)
    cut_comments = cut_sentences([c[1] for c in comments], output_file=splited_file, only_adj=True)

    # Words count
    wordcnt = Counter(chain.from_iterable(cut_comments))
    write_csv(wordcnt_file, wordcnt.most_common())

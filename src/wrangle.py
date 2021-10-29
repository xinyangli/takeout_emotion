import jieba
import re
from utils import *
from collections import Counter

if __name__ == '__main__':
    # Split sentence into words
    data_file = "../data/takeout_comment.csv"
    splited_file = "../data/splited.csv"
    wordcnt_file = "../data/wordcnt.csv"
    comments = read_csv(data_file)
    cut_comments = cut_sentences([c[1] for c in comments], output_file=splited_file)

    # Words count
    wordcnt = Counter()
    for splited_line in cut_comments:
        for word in splited_line: 
            wordcnt[word] += 1
    write_csv(wordcnt_file, wordcnt.most_common())

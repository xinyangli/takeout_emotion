
import jieba
import re
from utils import *
from collections import Counter

if __name__ == '__main__':
    # Split sentence into words
    data_file = "../data/takeout_comment.csv"
    splited_file = "../data/splited.csv"
    wordcnt_file = "../data/wordcnt.csv"
    punctuations = set([",", "，", "!", "！", "。", "?", "？", "~", "：", ":", ";", "；"])
    comments = ReadCSV(data_file)
    splited_list = []
    for comment in comments:
        seg_list = jieba.cut(comment[1], cut_all = True)
        splited_list.append([
            [seg for seg in seg_list if seg not in punctuations],
            comment[0]
        ])
    WriteCSV(splited_file, splited_list)

    # Words count
    wordcnt = Counter()
    for splited_line, emotion in splited_list:
        for word in splited_line: 
            wordcnt[word] += 1
    WriteCSV(wordcnt_file, wordcnt.most_common())

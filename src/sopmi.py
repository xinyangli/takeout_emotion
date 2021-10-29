#!/usr/bin/python
# -*- coding: utf-8 -*-
from utils import *
import jieba
import math


def get_PMI(nw1, nw2, nw12, n):
    p1 = nw1 / n
    p2 = nw2 / n
    if nw12 == 0:
        nw12 += 1  # Flatten data
        n += 1
    p12 = nw12 / n
    return math.log2(p12 / (p1 * p2))


def sopmi_result(positive_seeds, negative_seeds, comments):
    print('Counting words...')
    count = {}
    seed_cnt = {}
    for w in positive_seeds:
        seed_cnt[w] = 0
    for w in negative_seeds:
        seed_cnt[w] = 0
    occur = set()
    done = set()
    for comment in comments:
        occur.clear()
        done.clear()
        for word in comment:
            if word in done:
                continue
            if (word in positive_seeds) or (word in negative_seeds):
                occur.add(word)
                seed_cnt[word] += 1
                done.add(word)
        for word in comment:
            if word not in done:
                done.add(word)
                if word not in count:
                    temp = {'all': 0}
                    for w in positive_seeds:
                        temp[w] = 0
                    for w in negative_seeds:
                        temp[w] = 0
                    count[word] = temp
                for w in occur:
                    count[word][w] += 1
                count[word]['all'] += 1
    # WriteCSV(tmp_file, count)
    print('Calculating answers...')
    n = len(comments)
    result = []
    for key in count.keys():
        nw1 = count[key]['all']
        res = 0.0
        for w in positive_seeds:
            res += get_PMI(nw1, seed_cnt[w], count[key][w], n)
        for w in negative_seeds:
            res -= get_PMI(nw1, seed_cnt[w], count[key][w], n)
        if nw1 > 10:
            # result.append((res, key, nw1, [(seed_cnt[w], count[key][w]) for w in nseed], [(seed_cnt[w], count[key][w]) for w in pseed]))
            result.append((res, key))
    print('Sorting...')
    result.sort()
    return result


if __name__ == '__main__':
    source_file = '../data/takeout_comment.csv'
    result_file = '../data/result_sopmi.csv'
    # tmp_file = '../data/tmp.csv'
    punctuations = {',', '，', '!', '！', '。', '?', '？', '：', ':', ';', '；', '…', '/'}
    print('File reading...')
    comments_data = read_csv(source_file)
    pseed = {'好吃', '快'}
    nseed = {'难吃', '慢'}
    print('Writing results...')
    result = sopmi_result(pseed, nseed, comments_data)
    write_csv(result_file, result)

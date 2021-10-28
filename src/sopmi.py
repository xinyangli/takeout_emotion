from utils import *
import jieba
import math

def get_PMI(nw1, nw2, nw12, n):
    p1 = nw1 / n
    p2 = nw2 / n
    p12 = nw12 / n
    if p12 == 0:
        return 0.0
    return math.log2(p12 / (p1 * p2))

if __name__ == '__main__':
    source_file = '../data/takeout_comment.csv'
    result_file = '../data/result_sopmi.csv'
    #tmp_file = '../data/tmp.csv'
    punctuations = set([',', '，', '!', '！', '。', '?', '？', '~', '：', ':', ';', '；'])
    print('File reading...')
    comments = ReadCSV(source_file)
    pseed = ['好吃', '快']
    nseed = ['难吃', '慢']
    print('Counting words...')
    count = {}
    seed_cnt = {}
    for w in pseed:
        seed_cnt[w] = 0
    for w in nseed:
        seed_cnt[w] = 0
    occur = []
    done = []
    for comment in comments:
        occur.clear()
        done.clear()    
        words = jieba.lcut(comment[1], cut_all = True)
        for word in words:
            if word in done: continue
            if (word in pseed) or (word in nseed):
                occur.append(word)
                seed_cnt[word] += 1
                done.append(word)
        for word in words:
            if not ((word in punctuations) or (word in done)):
                done.append(word)
                if not word in count:
                    temp = {'all': 0}
                    for w in pseed:
                        temp[w] = 0
                    for w in nseed:
                        temp[w] = 0
                    count[word] = temp
                for w in occur:
                    count[word][w] += 1
                count[word]['all'] += 1
    #WriteCSV(tmp_file, count)
    print('Calculating answers...')
    n = len(comments)
    result = []
    for key in count.keys():
        nw1 = count[key]['all']
        res = 0.0
        for w in pseed:
            res += get_PMI(nw1, seed_cnt[w], count[key][w], n)
        for w in nseed:
            res -= get_PMI(nw1, seed_cnt[w], count[key][w], n)
        result.append((res, key))
    print('Sorting...')
    result.sort()
    print('Writing results...')
    WriteCSV(result_file, result)
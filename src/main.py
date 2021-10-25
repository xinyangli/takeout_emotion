import jieba
import OpenHowNet
import re
from utils import *
from collections import Counter

def init_dict(advanced = False):
    hownet_dict = OpenHowNet.HowNetDict(use_sim = advanced)
    return hownet_dict

def calculate_polarity(word, positive_seed, negative_seed, hownet_dict):
    if not hownet_dict.has(word):
        return 0
    for seed in positive_seed: 
        if word == seed:
            return 0
    for seed in negative_seed: 
        if word == seed:
            return 0
    positive_sum = negative_sum = 0
    max_score = 0
    for seed in positive_seed:
        score = hownet_dict.calculate_word_similarity(word, seed)
        positive_sum += score
        if max_score < score:
            max_score = score
    for seed in negative_seed:
        score = hownet_dict.calculate_word_similarity(word, seed)
        negative_sum += score
        if max_score < score:
            max_score = score
    if max_score < 0.5:
        return 0
    return positive_sum / len(positive_seed) - negative_sum / len(negative_seed)
    
if __name__ == "__main__":
    positive_seed_file = "../data/positive_seed.csv"
    negative_seed_file = "../data/negative_seed.csv"
    result_file = "../data/result.csv"
    theta = 0.001
    print("File reading......")
    positive_seed = ReadCSV(positive_seed_file)
    negative_seed = ReadCSV(negative_seed_file)
    word_list = ReadCSV("../data/wordcnt.csv")
    print("Init OpenHowNet......")
    hownet_dict = init_dict(advanced = True)
    print("Polarity calculating......")
    word_polarity = []
    for word, cnt in word_list:
        polarity = calculate_polarity(word, positive_seed[0], negative_seed[0], hownet_dict)
        if abs(polarity) > theta:
            word_polarity.append((polarity, word, cnt))
    word_polarity.sort()
    WriteCSV(result_file, word_polarity)
import jieba
import OpenHowNet
import re
from utils import *
from collections import Counter

def init_dict(advanced = False):
    if advanced:
        try:
            hownet_dict_advanced = OpenHowNet.HowNetDict(use_sim = True)
        except FileNotFoundError:
            OpenHowNet.download()
            hownet_dict_advanced = OpenHowNet.HowNetDict(use_sim = True)
        return hownet_dict_advanced
    try:
        hownet_dict = OpenHowNet.HowNetDict()
    except FileNotFoundError:
        OpenHowNet.download()
    return hownet_dict

def calculate_polarity(word, positive_seed, negative_seed, hownet_dict):
    positive_sum = negative_sum = 0
    for seed in positive_seed:
        positive_sum += hownet_dict.calculate_word_similarity(word, seed)
    for seed in negative_seed:
        negative_sum += hownet_dict.calculate_word_similarity(word, seed)
    return positive_sum / len(positive_seed) - negative_sum / len(negative_seed)
    
if __name__ == "__main__":
    positive_seed_file = "../data/positive_seed.csv"
    negative_seed_file = "../data/negative_seed.csv"
    positive_seed = ReadCSV(positive_seed_file)
    negative_seed = ReadCSV(negative_seed_file)
    hownet_dict = init_dict(advanced = True)
    word_list = ReadCSV("../data/wordcnt.csv")
    word_polarity = []
    for word, cnt in word_list:
        polarity = calculate_polarity(word, positive_seed[0], negative_seed[0], hownet_dict)
        word_polarity.append((polarity, word))
    word_polarity.sort()
    for polarity, word in word_polarity:
        print(word, polarity)
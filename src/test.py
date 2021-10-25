import OpenHowNet
from utils import *

positive_seed_file = "../data/positive_seed.csv"
negative_seed_file = "../data/negative_seed.csv"

hownet_dict = OpenHowNet.HowNetDict(use_sim = True)

positive_seed = ReadCSV(positive_seed_file)
negative_seed = ReadCSV(negative_seed_file)

positive_seed = positive_seed[0]
negative_seed = negative_seed[0]

word = "怪异"

for seed in positive_seed:
    x = hownet_dict.calculate_word_similarity(word, seed)
    print(seed, end = ' '), print(x)

for seed in negative_seed:
    x = hownet_dict.calculate_word_similarity(word, seed)
    print(seed, end = ' '), print(x)
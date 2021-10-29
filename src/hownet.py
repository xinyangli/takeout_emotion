import OpenHowNet


def init_dict(advanced = False):
    hownet_dict = OpenHowNet.HowNetDict(use_sim = advanced)
    return hownet_dict


def calculate_polarity(word, positive_seeds, negative_seeds, hownet_dict):
    if not hownet_dict.has(word):
        return 0
    for seed in positive_seeds:
        if word == seed:
            return 0
    for seed in negative_seeds:
        if word == seed:
            return 0
    positive_sum = negative_sum = 0
    max_score = 0
    for seed in positive_seeds:
        score = hownet_dict.calculate_word_similarity(word, seed)
        positive_sum += score
        if max_score < score:
            max_score = score
    for seed in negative_seeds:
        score = hownet_dict.calculate_word_similarity(word, seed)
        negative_sum += score
        if max_score < score:
            max_score = score
    if max_score < 0.5:
        return 0
    return positive_sum / len(positive_seeds) - negative_sum / len(negative_seeds)


def hownet_result(positive_seeds, negative_seeds, words, hownet_dict=None):
    theta = 0.001
    if hownet_dict is None:
        print("Init OpenHowNet......")
        hownet_dict = init_dict(advanced=True)
    result = []
    print("Polarity calculating......")
    for word in words:
        polarity = calculate_polarity(word, positive_seeds[0], negative_seeds[0], hownet_dict)
        if abs(polarity) > theta:
            result.append((polarity, word))
    result.sort()
    return result

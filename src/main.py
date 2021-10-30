from utils import *
from hownet import hownet_result
from sopmi import sopmi_result
from os.path import splitext

if __name__ == "__main__":
    pseed_file = "../data/positive_seed.csv"
    nseed_file = "../data/negative_seed.csv"
    result_file = "../data/result.csv"
    print("File reading......")
    pseed = read_csv(pseed_file)
    nseed = read_csv(nseed_file)

    # lines in wordcnt.csv are in (word, word_occurrence_count)
    word_occur = read_csv("../data/wordcnt.csv")
    word_occur = [c[0] for c in word_occur]

    write_csv(result_file, hownet_result(pseed, nseed, word_occur))
    pseed_sopmi = {"好吃", "快"}
    nseed_sopmi = {"难吃", "慢"}
    splited_comments = read_csv("../data/splited.csv")
    result_file, result_ext = splitext(result_file)
    write_csv(result_file + "_sopmi" + result_ext, sopmi_result(pseed_sopmi, nseed_sopmi, splited_comments))

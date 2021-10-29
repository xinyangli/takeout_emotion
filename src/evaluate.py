from utils import *
from main import *

def result_to_dict(result):
    result_dict = {}
    for line in result:
        (data, word) = line
        result_dict[word] = data
    return result_dict


def evaluate(main, reference):
    result = []
    for line in main:
        (data, word) = line
        calculate_polarity(word)
    return result


if __name__ == '__main__':
    main_result_file = '../data/result_sopmi.csv'
    reference_result_file = '../data/result.csv'
    main_result = read_csv(main_result_file)
    reference_result_file = read_csv(reference_result_file)
    reference_dict = result_to_dict(reference_result_file)

    write_csv('../data/compare.csv', evaluate(main_result, reference_dict))

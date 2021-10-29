import csv
import jieba


def read_csv(file):
    """
    Read data from csv file to memory
    """
    try:
        with open(file, newline='') as csvfile:
            datareader = csv.reader(csvfile)
            data = [x for x in datareader]
            csvfile.close()
        return data
    except FileNotFoundError as e:
        print(e)
        return []


def write_csv(file, dataset):
    with open(file, "w", newline='') as csvfile:
        datawriter = csv.writer(csvfile)
        datawriter.writerows(dataset)
        csvfile.close()


def cut_sentences(sentences, output_file=None):
    punctuations = {',', '，', '!', '！', '。', '?', '？', '：', ':', ';', '；', '…', '/'}
    splited_list = []
    for sentence in sentences:
        seg_list = jieba.cut(sentence, cut_all=False)
        # if output_file:
        #     splited_list.append(tuple([seg for seg in seg_list if seg not in punctuations]))
        # else:
        splited_list.append([seg for seg in seg_list if seg not in punctuations])
    if output_file is not None:
        write_csv(output_file, splited_list)
        return splited_list
    else:
        return splited_list

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


def cut_sentences(sentences, output_file=None, only_adj = False):
    punctuations = {',', '，', '!', '！', '。', '?', '？', '：', ':', ';', '；', '…', '/'}
    splited_list = []
    if only_adj is True:
        jieba.enable_paddle()
        import jieba.posseg as pseg
    for sentence in sentences:
        if only_adj is True:
            seg = pseg.cut(sentence, use_paddle=True)
            splited_list.append([word for (word, flag) in seg if flag == "a"])
        else:
            words = jieba.cut(sentence, cut_all=False)
            splited_list.append([word for word in words if word not in punctuations])
    if output_file is not None:
        write_csv(output_file, splited_list)
        return splited_list
    else:
        return splited_list

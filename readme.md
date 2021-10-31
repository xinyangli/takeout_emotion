## 项目描述

本项目使用 Jieba 分词和 HowNet 词典，使用基于**词典**的分析法和基于 **so-pmi** 的分析法两种算法，从接近 12000 条外卖评论中提取、分析、并筛选出了最具正负情感倾向性的 100 个词。

## 傻瓜式使用教学

```bash
# 建立虚拟环境并激活
python3 -m venv env
source env/bin/activate
# 安装依赖
pip install -r requirements.txt
# 安装字典
python
>>> import OpenHowNet
>>> OpenHowNet.download()
>>> exit()
```

然后先执行 wrangle.py，后执行 main.py。就可以在 data 里看到 result 了捏。

## 数据文件描述

预设文件：

1. negative_seed.csv, positive_seed.csv 存放基于 HowNet 的情感倾向性分析所使用的种子词

2. takeout_comment.csv 存放原始的评论集

生成文件：（部分是调试、研究过程中生成的，这里不作介绍）

1. splited.csv 分词后的结果

2. wordcnt.csv 所有出现过的词以及它的词频

3. result.csv, result_sopmi.csv 利用两种不同算法分析排序后的结果

## 接口描述

1. utils.py

  read_csv(file)：传入字符串（文件目录），返回一个列表，即读取到的，每行的内容。

  write_csv(file, dataset): 传入字符串（文件目录）和待写入的数据，写进去的每个元素占一行。

  cut_sentences(sentences, output_file=None, only_adj = False)：传入待分词的句子，输出的文件，以及是否只保留形容词，返回一个列表，存放分出来的词

2. sopmi.py

  get_PMI(nw1, nw2, nw12, n): 计算两个词的 PMI 值，传入的是第一个词出现的次数、第二个词出现的次数、两个词共现的次数、语句的总数。返回 PMI 值。

  sopmi_result(positive_seeds, negative_seeds, comments): 传入积极种子词集和消极种子词集，以及分过词的评论集，返回的是计算并排序后的词语列表。

3. hownet.py

  init_dict(advanced = False): 返回初始化后的 HowNet 词典。advanced 参数表示这个词典是否要用于相似度计算。

  calculate_polarity(word, positive_seeds, negative_seeds, hownet_dict): 传入待计算词、正向种子词集、负向种子词集、和初始化过的词典对象，返回计算出的语义倾向值。

  hownet_result(positive_seeds, negative_seeds, words, hownet_dict=None): 传入正向种子词集、负向种子词集、待计算词语集、词典（没有会字典创建），返回计算并排序后的答案列表。
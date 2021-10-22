# 实验：对外卖评论中词语的情感分析

实验环境 Ubuntu - 20.04

使用的两个包：[jieba 分词](https://github.com/fxsjy/jieba) [OpenHowNet](https://github.com/thunlp/OpenHowNet)

~~快住手，你这不是在写 readme，是在写实验报告~~

## 一、项目文件及其功能介绍

1. **data** 文件夹

   | 文件名              | 功能或内容   |
   | :-----------------: | :----------: |
   | takeout_comment.csv | 所有外卖评论 |
   | splited.csv |初步分词处理后得到的词语|
   | wordcnt.csv |词频统计（词语去重）的结果|
   | positive_seed.csv |消极种子词|
   | negative_seed.csv |积极种子词|
   | result.csv |按词语的语义倾向值的排序结果，也就是实验结果|
   
2. **src** 文件夹

	|   文件名   |      功能或内容      |
	| :--------: | :------------------: |
	|  utils.py  | 便捷的 csv 读写接口  |
	| wrangle.py |    分词及词频统计    |
	|  main.py   | 计算语义倾向值并排序 |

## 二、实验准备

```bash
# 在 takeout_emotion 目录下执行下面的指令
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

## 三、实验步骤

1. 写代码（废话）
2. 把设计的种子词写进那两个 csv 文件中
3. 运行 wrangle.py 分词
4. 运行 main.py 计算并查看结果
5. ~~修改 main.py 里的参数和种子词，继续玩~~

## 四、重要接口

|                            函数名                            |                             功能                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| calculate_polarity(word, positive_seed, negative_seed, hownet_dict) | 两个 seed 是种子词列表，需要一个已经初始化的字典 hownet_dict，会根据这两个列表和公式计算 word 的倾向值 |
|                        ReadCSV(file)                         | file 是字符串，表示目标文件的路径，会读取这个文件的内容，并返回一个列表 |
|                   WriteCSV(file, dataset)                    |          将这个列表 dataset 写入路径为 file 的文件           |


import jiagu
from tqdm import tqdm
import re
import numpy as np
import pandas as pd
# df = pd.read_csv("sanguo2.xls", usecols=[1], encoding="utf-8")
# gb18030
# 读取csv文件，主要是提取人物名字
df = pd.read_csv("sanguo2.csv", skiprows=[0],usecols=[1], encoding="utf-8")
# print(df)
a = []
data_array = np.array(df.stack())
data_list = data_array.tolist()

print(data_list)
"""
# 读取文件
file1 = open("sanguoyanyi.txt", "r", encoding="utf-8")
# 去掉多余的换行
text = file1.read().strip()
file1.close()
# print(text)
# 发现有特殊符号“-”，用re去掉
text = re.sub(r'-','',text)
# print(text)
# jiagu.ner不能传入str类型,将其转为list
text = re.split("[,。;\n]", text)
# print(text)
sanguo_ner = []
for sentences in text:
    sentences = jiagu.seg(sentences)
    sentences = jiagu.ner(sentences)
    sanguo_ner.append(sentences)
print(sanguo_ner)
# print(len(text))
# 实体识别
# print("识别中……")
# 不能传入str类型
# words = tqdm(jiagu.ner(text))

# print("识别完毕")


text = '厦门明天会不会下雨'

words = jiagu.seg(text) # 分词
print(words)


ner = jiagu.ner(words) # 命名实体识别
print(ner)
"""


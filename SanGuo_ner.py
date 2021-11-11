import jiagu
from tqdm import tqdm
import re


file1 = open("去停用词后分词目录.txt", "r", encoding="utf-8")
text = file1.read()
file1.close()

# 去掉之前带的单词数量数字
text = re.sub("[0-9]","",text)
print(text)
words = []
for i in text:
    words.append(i)
print(words)

# 实体识别
sanguo_ner = []
for sentences in text:
    sentences = jiagu.seg(sentences)
    sentences = jiagu.ner(sentences)
    sanguo_ner.append(sentences)
# print(sanguo_ner)

nvs = zip(words, sanguo_ner)
nvDict = dict((words, sanguo_ner) for words, sanguo_ner in nvs)
print(nvDict)
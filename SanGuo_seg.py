import jiagu
from tqdm import tqdm
# import pandas as pd
import re
# import jieba
# 词云
import wordcloud

def takeSecond(elem):
    # 排序用
    return elem[1]

def main():
    # 读取文件
    file1 = open("sanguoyanyi.txt", "r", encoding="utf-8")
    text = file1.read()
    file1.close()
    # print(text)

    # 发现有特殊符号“-”，用re去掉
    # text = re.sub(r'-','',text)
    # print(text)
    #按逗号、句号、分号、换行进行分句
    # text = re.split("[,。;\n]", text)
    # print(text)

    # 分词
    print("分词中……")
    # words = tqdm(jiagu.seg(text))
    words = jiagu.seg(text)
    # jieba分词
    # words = jieba.lcut(text)
    print("分词完毕！")

    # 词语  数量
    counts = {}

    for word in words:
        # 不要一个字的
        if len(word) == 1:
            continue
        # 同人不同称呼合并
        elif word == "孔明" or word == "诸葛孔明":
            rword = "诸葛亮"
        elif word == "关公" or word == "云长" or word == "关云长":
            rword = "关羽"
        elif word == "玄德" or word == "刘玄德"or word == "皇叔" or word == "先主":
            rword = "刘备"
        elif word == "翼德" or word == "张翼德":
            rword = "张飞"
        elif word == "后主" or word == "阿斗":
            rword = "刘禅"
        elif word == "孟德" or word == "曹孟德" or word == "曹阿瞒":
            rword = "曹操"
        elif word == "子龙" or word == "赵子龙":
            rword = "赵云"
        elif word == "奉先" or word == "吕奉先":
            rword = "吕布"
        # 太多了，就先弄这些
        else:
            rword = word
        counts[rword] = counts.get(rword,0) + 1
        

    # 去停用词
    file = open("stopwords.txt","r", encoding="utf-8")   
    excludes =file.read().split("\n") 
    file.close()
    # print(excludes)
    for delWord in excludes:
        try:
            del counts[delWord]
        except:
            continue

    
    items = list(counts.items())
    # 从数量多到少排序
    items.sort(key = takeSecond,reverse=True)   

    f= open("去停用词后分词目录_带数量.txt","w+")
    for i in range(len(items)):
        item=items[i]
        keyWord =item[0]
        count=item[1]
        # print("{0:<10}{1:>5}".format(keyWord,count))
        # 带数量
        f.write("{0:<10}{1:>5}\n".format(keyWord,count))
        # 不带数量
        # f.write("{0:<10}\n".format(keyWord))
    f.close()

    # 生成词云,得把字体放到当前项目根目录
    wc = wordcloud.WordCloud(font_path="msyh.ttf",width=1000,height=500,background_color="white")
    wc.generate(str(items[0:20]))
    wc.to_file("三国演义词云图.jpg")

    # 根据词云发现问题，有“将军”、“丞相”等无法分辨是哪位将军或丞相，亟待解决

main()

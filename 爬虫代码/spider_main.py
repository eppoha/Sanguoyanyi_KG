#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html_downloader, html_outputer,  url_manager
import html_parser
import importlib,sys
importlib.reload(sys)
import numpy as np
import pandas as pd
class SpiderMain(object):
    def __init__(self):

        # url管理器
        self.urls = url_manager.UrlManager()

        # 下载器
        self.downloader = html_downloader.HtmlDownloader()

        # 解析器
        self.parser = html_parser.HtmlParser()

        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1

        # 初始url
        self.urls.add_new_url(root_url)
        
        # 获取待爬取url
        new_url = self.urls.get_new_url()
        # 启动下载器下载页面
        html_cont = self.downloader.download(new_url)

        # 启动解析器将新的url和爬到的数据进行保存
        # new_urls, new_data = self.parser.parse(new_url, html_cont)
        now_data = self.parser.parse(new_url, html_cont)

        # 将新的url添加
        # self.urls.add_new_urls(new_urls)

        # 收集爬取数据
        self.outputer.collect_data(now_data)

        """
        # 当存在可爬取的url时
        while self.urls.has_new_url():
            try:
                # 获取待爬取url
                new_url = self.urls.get_new_url()

                print('craw %d: %s' % (count, new_url))

                # 启动下载器下载页面
                html_cont = self.downloader.download(new_url)

                # 启动解析器将新的url和爬到的数据进行保存
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                # 将新的url添加
                self.urls.add_new_urls(new_urls)

                # 收集爬取数据
                self.outputer.collect_data(new_data)

                # 爬取5个网页
                if count == 5:
                    break
                count += 1

            except:
                print('craw failed')

        """
        # 输出内容
        self.outputer.output_html()


if __name__ == '__main__':
    # 最终爬取365条数据，可能是有的人物百度百科没有收录
    # import pandas as pd
    
    # 读取csv文件，主要是提取人物名字
    df = pd.read_csv("sanguo2.csv",usecols=[1], encoding="utf-8")
    data_array = np.array(df.stack())
    # 转换成列表
    data_list = data_array.tolist()
    # print(df)

    obj_spider = SpiderMain()
    root_url = 'https://baike.baidu.com/item/'
    r_url = ''
    for i in data_list:
        r_url = ''
        # 会报错，
        # 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
        # 汉字无法传参，需要转译
        r_url = root_url+str(i)
        print(r_url)
        # 开始爬取
        obj_spider.craw(r_url)
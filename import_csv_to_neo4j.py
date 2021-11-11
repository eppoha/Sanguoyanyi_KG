# 先看一下现有的资料
import pandas as pd
# df = pd.read_csv("triples.csv")
# print(df)

from py2neo import Graph
# 连接本地的 Neo4j 数据库，地址为 127.0.0.1，http 端口默认为 7474，用户名和密码分别为 neo4j 与 123
graph = Graph(host='127.0.0.1', http_port=7474, user='neo4j', password='123')
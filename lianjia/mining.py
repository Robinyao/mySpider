import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import json

# 读取json文件
jsondata = json.load(open('./houses.json'))
# 转换为DataFrame
df = DataFrame(jsondata)
# 保存为csv文件
df.to_csv('houses.csv', sep=';', encoding='utf-8', header=None)
# 去掉所有'.'点号 (1，去掉多余数据； 2，日期数字化)
# sed -i 's/\.//g'

# 读取csv文件
data = pd.read_csv('./houses.csv', sep=';')
# 副本
df0 = data
# 添加新列： 价格/面积
df0['fate'] = pd.Series(df0['price']/df0['square'], index=df0.index)
# 排序
df0 = df.sort_values(by=['fate', 'square'])
# 选择列
df1 = df0[['address', 'floor', 'link_url', 'rooms', 'square', 'price', 'uptime']]
# 选择发布时间
df2 = df1[df1['uptime'] > 20160820]
# 选择价格
df3 = df2[df2['price'] < 4500]
# 选择时间
df4 = df3[df['uptime'] > 20160820]
# 选择户型

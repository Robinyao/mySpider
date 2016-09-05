import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import json

# 读取json文件
# jsondata = json.load(open('./houses.json'))
# 转换为DataFrame
# df = DataFrame(jsondata)
# 保存为csv文件
# df.to_csv('houses.csv', sep=';')

# 读取csv文件
data = DataFrame('./houses.csv', sep=';')
# 副本
df0 = data
# 添加新列： 价格/面积
df0['fate'] = pd.Series(df0['price']/df0['square'], index=df0.index)
# 排序
df0 = df.sort_values(by=['fate', 'price', 'square'])
#df0 = data.sort_values(by=['price', 'square'], ascending=[False, False])

df2 = df.sort_values(by=['fate', 'price', 'square'])

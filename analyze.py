'''
import pandas as pd
df = pd.read_csv("合并-耳机.csv")
for index in range(df["rate"].count()):
    df["rate"][index] = df["rate"][index].strip()
df.to_csv("合并-耳机.csv", index=False, sep=',')

with open("合并-耳机.csv", "r", encoding="utf-8") as file:
    for line in file:
        print(line)
'''
'''
def percent2float(rate):
    return float(rate.strip('%'))

import pandas as pd
df = pd.read_csv("合并-耳机.csv")
df['rate'] = df['rate'].apply(lambda x: percent2float(x))
'''
'''
import pandas as pd
df = pd.read_csv("合并-耳机.csv")
df = df.sort_values(by='rate',ascending=False)
df.to_csv("合并-耳机.csv", index=False, sep=',')
'''
'''
import pandas as pd
df = pd.read_csv("合并-防晒.csv")
df.rename(columns={'商品名称':'name', '商品图片':'pic', '商品链接':'url', 
        '商品价格':'price'},inplace=True) 
df.dropna(subset=['rate'],inplace=True)
df.to_csv("合并-防晒.csv", index=False, sep=',')
'''
import pandas as pd
import os
def normalization(rate):
    return float((rate.strip()).strip('%'))

filepath = 'E:\\大三上课件\\软件工程（k班）\\数据整合\\合并2'
filelist = os.listdir(filepath)
for file in filelist:
    filename = filepath  + '\\' + file
    df = pd.read_csv(filename)
    df.rename(columns={'商品名称':'name', '商品图片':'pic', '商品链接':'url', 
        '商品价格':'price'},inplace=True) 
    df.dropna(subset=['rate'],inplace=True)
    df['rate'] = df['rate'].apply(lambda x: normalization(x))
    df = df.sort_values(by='rate',ascending=False)
    print(file + " succeed to normalize!")
    df.to_csv(filename, index=False, sep=',')
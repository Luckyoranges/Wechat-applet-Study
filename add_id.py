import pandas as pd
import os
'''
def normalization(sales):
    return sales[0:sales.find('+')]
filepath = 'E:\\大三上课件\\软件工程（k班）\\Beta\\电子产品'
filelist = os.listdir(filepath)
for file in filelist:
    filename = filepath  + '\\' + file
    df = pd.read_csv(filename)
    df['sales'] = df['sales'].apply(lambda x: normalization(x))
    df.to_csv(filename, index=False, sep=',')
'''
'''
def Str2Float(sales):
    if sales[-1] == '万':
        sales = sales[0:-1]
        return float(sales)*10000
    else:
        return float(sales)

filepath = 'E:\\大三上课件\\软件工程（k班）\\Beta\\电子产品'
filelist = os.listdir(filepath)
for file in filelist:
    filename = filepath  + '\\' + file
    df = pd.read_csv(filename)
    df['sales'] = df['sales'].apply(lambda x: Str2Float(x))
    df.to_csv(filename, index=False, sep=',')
'''
'''
df = pd.read_csv('oppo.csv')
df.sort_values(by=['sales','price'],ascending=[False, True], inplace=True)
df.to_csv('oppo.csv', index=False, sep=',')
'''
def normalization(sales):
    return sales[0:sales.find('+')]

def Str2Float(sales):
    if sales[-1] == '万':
        sales = sales[0:-1]
        return float(sales)*10000
    else:
        return float(sales)

filepath = 'E:\\大三上课件\\软件工程（k班）\\Beta\\食品饮料'
filelist = os.listdir(filepath)
for file in filelist:
    filename = filepath  + '\\' + file
    df = pd.read_csv(filename)
    df['id'] = ''
    for index in range(df['sales'].count()):
        url = df['url'][index]
        df.loc[index, 'id'] = str(url[20:url.find(".html")])
    df['sales'] = df['sales'].apply(lambda x: normalization(x))
    df['sales'] = df['sales'].apply(lambda x: Str2Float(x))
    df.sort_values(by=['sales','price'],ascending=[False, True], inplace=True)
    df.to_csv(filename, index=False, sep=',')
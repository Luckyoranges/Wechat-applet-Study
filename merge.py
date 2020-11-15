import pandas as pd
f1 = pd.read_csv('3M便利贴.csv')
f2 = pd.read_csv('便利贴.csv')
file = [f1,f2]
train = pd.concat(file,axis=1)
train.to_csv("合并.csv", index=0, sep=',')
import pandas as pd
'''
url = "https://item.jd.com/100006510545.html"
print(url[20:url.find(".html")])
'''
df = pd.read_csv("合并-耳机.csv")
df['id'] = ''
for index in range(df['rate'].count()):
    url = df['url'][index]
    df.loc[index, 'id'] = str(url[20:url.find(".html")])
df.to_csv("合并-耳机.csv", index=False, sep=',')
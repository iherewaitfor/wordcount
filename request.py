import requests
from pathlib import Path
# -*- coding: utf-8 -*- 
import sys
import io
from textrank4zh import TextRank4Keyword

response  = requests.get("https://www.baidu.com")
print(type(response))
print(response.status_code)
# print(type(response.text))

# print(response.headers)
# print(response.headers['content-type'])

# print(response.request.headers)

# response.enconding = "utf-8"

# print(response.cookies)

# print(response.content)
# print(response.content.decode("utf-8"))
text = response.content.decode("utf-8")

tr4w = TextRank4Keyword()
tr4w.analyze(text=text, lower=True, window=2)
strTemp = ''
i = 0
pathPre = "./requesttxt"
filePath = pathPre + ".txt"
txtFile = Path(filePath)
while txtFile.exists():
    filePath = pathPre + str(i) +".txt"
    i +=1
    txtFile = Path(filePath)

with open(filePath,'w') as f:
    for words in tr4w.words_all_filters:
        f.write('/'.join(words))
        strTemp += '/'.join(words)
print(strTemp)
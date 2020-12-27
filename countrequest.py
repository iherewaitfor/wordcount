#_*_coding:utf-8_*_
import pandas as pd

text = open("requesttxt.txt").read()
li=text.split("/")
counte_phrase_phrase=[]
counte_phrase_times=[]
for i in range(10):
    counte_phrase_times.append(text.count(li[i]))
    counte_phrase_phrase.append(li[i])
pdf=pd.DataFrame({"phrase":counte_phrase_phrase,
                   "times":counte_phrase_times}).sort_values("times",ascending=False)
print(pdf)
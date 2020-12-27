 #-*- coding: UTF-8 -*-   
import jieba
import io
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 统计特定词汇在 文件中出现的次数

# cha = [u'安全',u'知乎',u'食品',u'安全法',u'食品安全法']
cha = []
with io.open("wordsneedcount.txt", "r",encoding ='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')  #去掉列表中每一个元素的换行符
        print(line)
        cha.append(line)
# 加入特定词汇进行分词
for key in cha:
    jieba.add_word(key)

# 打开特定文件
txt = io.open('zhihu.txt','r', encoding ='utf-8').read()
# jieba.lcut() 精确模式切分中文
txt = jieba.lcut(txt)
counts = {}
# cha = [u'安全',u'知乎',u'食品',u'安全法',u'食品安全法']
new = {}
# string.format() 格式化
print(u'给定的{}个词汇的统计:'.format(len(cha)))
for word in txt:
    #过滤单文本
    if len(word) == 1:
 		continue
    else:
        rword = word
 	counts[rword] = counts.get(rword,0) + 1
for key,value in counts.items():
	if key in cha:
		new[key] = value
li = list(new.items())
# print('/'.join(li))
#由大到小排序

# 插入没有在结果中出现的特定词汇到结果中
for key in cha:
    bFind = False
    for k,v in li:
        if key == k:
            bFind = True
    if bFind != True:
        li.append((key,0))
li.sort(key=lambda x:x[1], reverse=True)
print(str(len(li)))
# for i in range(1,len(li)+1):
# 	key,value = li[i-1]
# 	print('{:<3}{:<6}{:>5}'.format(i,key.encode("gbk"),value))

with io.open("countwordsout.txt", "w",encoding ='utf-8') as f:
    for i in range(1,len(li)+1):
        key,value = li[i-1]
        temStr = '{:<3}{:<16}{:>5}'.format(i,key.encode("gbk"),value)
        print(temStr)
        temStr +='\n'
        f.write(unicode(temStr, "gbk"))
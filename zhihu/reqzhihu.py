# -*- coding: utf-8 -*- 
import requests
import json
import io

 
def fetchHotel(url):
    # 发起网络请求，获取数据
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    }
 
    # 发起网络请求
    r = requests.get(url,headers=headers)
    r.encoding = 'Unicode'
    return r.text
 
def parseJson(text,f):
    json_data = json.loads(text)
    lst = json_data['data']
    nextUrl = json_data['paging']['next']
    
    if not lst:
        return
 
    for item in lst:
        type = item['target']['type']
        
        if type == 'answer':
            # 回答
            question = item['target']['question']
            id = question['id']
            title = question['title']
            url = 'https://www.zhihu.com/question/' + str(id)
            # print(u"问题：",id,title)
            temStr = '{:<3}{:<16}{}'.format(u"回答:".encode("gbk"),id ,title.encode("gbk"))
            print(temStr)
            temStr +='\n'
            f.write(unicode(temStr, "gbk"))

 
        elif type == 'article':
            #专栏
            zhuanlan = item['target']
            id = zhuanlan['id']
            title = zhuanlan['title']
            url = zhuanlan['url']
            vote = zhuanlan['voteup_count']
            cmts = zhuanlan['comment_count']
            auth = zhuanlan['author']['name']
            #print("专栏：",id,title.encode('gbk'))
            temStr = '{:<3}{:<16}{}'.format(u"专栏:".encode("gbk"),id ,title.encode("gbk"))
            print(temStr)
            temStr +='\n'
            f.write(unicode(temStr, "gbk"))
 
        elif type == 'question':
            # 问题
            question = item['target']
            id = question['id']
            title = question['title']
            url = 'https://www.zhihu.com/question/' + str(id)
            # print("问题：",id,title)
            # temStr = '{:<3}{:<16}{}'.format(u"问题:".encode("gbk"),id ,title.encode("gbk"))
            # print(temStr)
            # temStr +='\n'
            # f.write(unicode(temStr, "gbk"))
 
    return nextUrl
 
if __name__ == '__main__':
    #topicID = '20192351' 
    topicID = '19855668' 
    url = 'https://www.zhihu.com/api/v4/topics/' + topicID + '/feeds/top_activity?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&after_id=0'
    with io.open("zhihu.txt", "w",encoding ='utf-8') as f:
        while url:
            text = fetchHotel(url)
            url = parseJson(text, f)
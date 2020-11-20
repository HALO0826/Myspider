import requests
import json
# 聚焦爬虫：获得页面局部信息
if __name__ == "__main__":
    post_url = 'https://fanyi.baidu.com/sug'
    kw = input('enter a word:\n')
    data = {
        'kw': kw
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Mobile Safari/537.36 Edg/86.0.622.69 '
    }
    response = requests.post(url=post_url, params=data, headers=header)
    # .text返回的是txt，.json返回的是json(obj) 必须确认响应类型(content-type)是json格式
    result = response.json()
    fp = open('02 files/'+kw, 'w', encoding='utf-8')
    json.dump(result, fp=fp)
    print(result)

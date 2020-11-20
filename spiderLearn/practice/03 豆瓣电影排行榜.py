import requests
import json
# 聚焦爬虫：获得页面局部信息
if __name__ == "__main__":
    post_url = 'https://movie.douban.com/j/chart/top_list'
    data = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '1',
        'limit': '20',
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Mobile Safari/537.36 Edg/86.0.622.69 '
    }
    response = requests.get(url=post_url, params=data, headers=header)
    # .text返回的是txt，.json返回的是json(obj) 必须确认响应类型(content-type)是json格式
    result = response.json()
    fp = open('03/喜剧', 'w', encoding='utf-8')

    json.dump(result, fp=fp)

    print(result)
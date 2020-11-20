import requests

# 反爬机制: UA监测:门户网站服务器会检测对应请求的载体身份表识，
# 如果监测到的载体未某浏览器，说明该请求是正常的，服务器就不会拒绝请求，
# 如果监测到的不是某款浏览器，则会视为不正常请求，服务器就会拒绝请求
# UA: User Agent
# UA伪装:将爬虫的UA伪装成某一款浏览器
if __name__ == '__main__':
    # 找浏览器搜索网页url ?之后是url参数，在请求中处理参数
    url = 'https://www.sogou.com/web'
    kw = input('enter a word')
    param = {
        'query': kw
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Mobile Safari/537.36 Edg/86.0.622.69 '
    }
    response = requests.get(url=url, params=param, headers=header)
    page_text = response.text
    fileName = './01 html/'+kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('保存成功')

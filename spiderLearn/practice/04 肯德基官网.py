import requests
import json

# 聚焦爬虫：获得页面局部信息
if __name__ == "__main__":
    city_name = input("请输入城市名字:\n")

    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': city_name,
        'pid': '',
        'pageIndex': '1',
        'pageSize': '10',
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Mobile Safari/537.36 Edg/86.0.622.69 '
    }
    response = requests.post(url=post_url, params=data, headers=header)
    result = response.text
    result = json.loads(result)

    page_number = int(result["Table"][0]['rowcount'])
    page_number = int(page_number / 10)

    fp = open('04/' + data['cname'], 'w', encoding='utf-8')
    for j in range(0, 10):
        fp.write(str(result['Table1'][j]) + '\n')

    print(page_number)
    for i in range(2, page_number + 1):
        data = {
            'cname': city_name,
            'pid': '',
            'pageIndex': i,
            'pageSize': '10',
        }
        response = requests.post(url=post_url, params=data, headers=header)
        result = json.loads(response.text)
        for j in range(0, 10):
            fp.write(str(result['Table1'][j]) + '\n')

    fp.close()

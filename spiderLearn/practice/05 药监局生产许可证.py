import requests
import json

if __name__ == "__main__":
    # 批量抓取企业ID
    post_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.198 Mobile Safari/537.36 Edg/86.0.622.69 '
    }
    # 存放于数组中
    page_range1 = input("请输入爬取的前页码:\n")
    page_range2 = input("请输入爬取的后页码:\n")
    print('正在爬取......')

    id_list = []
    for i in range(int(page_range1), int(page_range2)):
        data = {
            "on": "true",
            "page": i,
            "pageSize": "15",
            "productName": "",
            "conditionType": "1",
            "applyname": "",
            "applysn": "",
        }
        response = requests.post(url=post_url, params=data, headers=header)
        result = response.json()
        for j in range(0, 15):
            id.append(result['list'][j]['ID'])

    f = open('./05/药监', 'w', encoding='utf-8')
    # 有了ID数组后，批量post请求获取数据
    for i in range(0, len(id_list)):
        url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
        data = {
            'id': id_list[i]
        }
        response = requests.post(url, data, header)
        f.write(response.text + '\n')

    f.close()
    print('ok!')

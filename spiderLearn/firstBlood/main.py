import requests

url = 'http://www.mvcat.com/'
response = requests.get(url=url)
page_text = response.text
print(page_text)

with open('./mvcat.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)

print('存储完成')
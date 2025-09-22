import requests
from lxml import etree
import os

# 下载的图片库地址
url = 'http://www.netbian.com/mei/'

# 伪装请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}

resp = requests.get(url, headers=headers)
resp.encoding = 'gbk'
# print(resp.text)

r = etree.HTML(resp.text)
# 获取图片路径
srcList = r.xpath('//div[@class="list"]/ul/li/a/img/@src')
# 获取图片名称
nameList = r.xpath('//div[@class="list"]/ul/li/a/img/@alt')

# 获取当前脚本文件所在的目录
currentPath = os.path.dirname(os.path.abspath(__file__))
# print(currentPath)

for src, name in zip(srcList, nameList):
    print(f'图片名称:{name}, 图片地址{src}', '开始下载')
    with open(os.path.join(currentPath, 'imgs', f'{name}.jpg'), 'wb') as f:
        f.write(requests.get(src, headers=headers).content)


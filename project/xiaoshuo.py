import requests

from lxml import etree


# 章节变量
chapter_count = 1


# 获取内容
def get_content(url):
    # print('请求的url', url)
    # 伪装请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }

    resp = requests.get(url, headers=headers)
    # 设置编码
    resp.encoding = "utf-8"

    # print(resp.text)

    # 解析网页
    e = etree.HTML(resp.text)
    info = "\n".join(e.xpath('//div[@class="m-post"]/p/text()'))
    # print(info)
    title = e.xpath('//div[@class="entry-tit"]/h1/text()')[0]
    # 保存网页
    global chapter_count
    with open(f"斗罗大陆{chapter_count}.txt", "w", encoding="utf-8") as f:
        f.write(title + "\n\n" + info + "\n\n")

    # 获取下一章
    chapter_count += 1
    next_url = "https://dl.131437.xyz" + e.xpath("//tr/td[2]/a/@href")[0]
    print(next_url)
    if next_url.endswith(".html"):
        get_content(next_url)
    else:
        print("小说获取完毕！！！！")


def main():
    url = "https://dl.131437.xyz/book/douluodalu5/2128330.html"
    get_content(url)


if __name__ == "__main__":
    main()

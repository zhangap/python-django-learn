# 需求：
# 1、把video.xlsx中的，以国家进行分类，分别存储在对应的sheet页中，方便以国家分类进行查找
# 2、把类别中的上映时间分离出来，作为单独的一列进行展示

import pandas as pd


def main():
    # 读取excel文件
    data = pd.read_excel('video.xlsx')
    data['上映时间'] = data['类别'].apply(lambda x: x.split('/')[0].strip())
    data['类别'] = data['类别'].apply(lambda x: formatType(x))
    # print(data)
    writer = pd.ExcelWriter('格式化后数据.xlsx')

    for country in data['国家'].unique():
        print(country)
        data[data['国家'] == country].to_excel(writer, sheet_name=country)

    writer.close()


# 格式化类别(去掉上映时间，保留其他)
def formatType(data):
    res = data.split('/')
    return '/'.join(res[1: len(res)])


if __name__ == '__main__':
    main()

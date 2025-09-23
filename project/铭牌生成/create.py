import os

import pandas as pd

from docxtpl import DocxTemplate

current_path = os.path.dirname(os.path.abspath(__file__))

data = pd.read_excel(os.path.join(current_path, '名单.xlsx'))
person_list = []

for index, row in data.iterrows():
    person_list.append({
        'name': row['name'],
        'company': row['company'],
        'title': row['title'],
    })
# print(person_list)

context = {
    'person_list': person_list,
}
doc = DocxTemplate(os.path.join(current_path, 'template.docx'))
# 渲染模板
doc.render(context)
# 保存生成新文档
doc.save('铭牌文档.docx')

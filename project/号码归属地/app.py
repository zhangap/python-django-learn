import requests
from flask import Flask, request, render_template, jsonify

from lxml import etree

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['GET'])
def query():
    phone = request.args.get('phone')
    area = get_mobile(phone)
    return jsonify({
        'message': area
    })


def get_mobile(phone):
    url = f'https://ip138.com/mobile.asp?mobile={phone}&action=mobile'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'

    e = etree.HTML(resp.text)
    datas = e.xpath('//tr/td[2]/span/text()')
    print(datas)
    return datas


app.run(debug=True)

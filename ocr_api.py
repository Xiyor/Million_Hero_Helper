# coding:utf-8
import urllib, urllib.request, base64
import json


def access_token_obtain():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    AK = "???"
    SK = "???"
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(AK, SK)
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        print(content)

# access_token = access_token_obtain()

def baidu_ocr_api():

    access_token = '???'
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
    # 二进制方式打开图文件
    f = open(r'screenshot.jpg', 'rb')
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.parse.urlencode(params).encode('utf-8')
    request = urllib.request.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    res = ""
    if (content):
        content = json.loads(str(content, encoding='utf-8'))
        for ele in content['words_result']:
            res += ele['words']
    print("wd: {}".format(res))
    return res

baidu_ocr_api()
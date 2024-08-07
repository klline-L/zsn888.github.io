# -*- coding: utf-8 -*-
import random
import xlrd
from sanic import Sanic
from sanic import response

app = Sanic('myapp')

filename = "life64.xlsx"
data = xlrd.open_workbook(filename)
table = data.sheets()[0]


@app.get('/life')
def life(request):

    number = random.randint(0, 63)
    luck_type = table.row_values(number)[2][:-1]

    if luck_type in ["上上"]:
        word = "恭喜！抽到上上签！"
    elif luck_type in ["下下"]:
        word = "哦豁！抽到下下签！别灰心再来一次"
    else:
        word = "这次抽中的是：{}签！".format(luck_type)

    message = {
        "前言": word,
        "抽到的卦为": table.row_values(number)[0],
        "卦名": table.row_values(number)[1],
        "解卦": table.row_values(number)[3]
    }
    html_message = f"""
    <body><p style="color: pink">郑淑宁专属抽签抢先版</p>
    <h4>{word}</h4>
    <p>抽到的卦为：{table.row_values(number)[0]}</p>
    <p>卦名：{table.row_values(number)[1]}</p>
    <p>解卦：{table.row_values(number)[3][3:50]}</p>
    <p>      {table.row_values(number)[3][50:]}</p>
    <p>      input()</p>
    <br>
    <p style="color: pink">仅供娱乐。</p>
</body>
    """
    return response.html(html_message)


@app.get('/better')
def better(request):
    lucky_number = [0, 1, 7, 13, 20, 26, 41, 42, 45, 47, 48, 52, 54, 57, 59]

    number = random.choice(lucky_number)
    luck_type = table.row_values(number)[2][:-1]

    if luck_type in ["上上"]:
        word = "恭喜！抽到上上签！"
    elif luck_type in ["下下"]:
        word = "哦豁！抽到下下签！"
    else:
        word = "抽中的是：{}签！".format(luck_type)

    message = {
        "前言": word,
        "抽到的卦为": table.row_values(number)[0],
        "卦名": table.row_values(number)[1],
        "解卦": table.row_values(number)[3]
    }
    html_message = f"""
        <body>
        <h4>{word}</h4>
        <p>抽到的卦为：{table.row_values(number)[0]}</p>
        <p>卦名：{table.row_values(number)[1]}</p>
        <p>解卦：{table.row_values(number)[3][3:50]}</p>
        <p>      {table.row_values(number)[3][50:]}</p>
        <br>
        <img>
        <p style="color: red">郑淑宁专属。</p>
    </body>
        """
    return response.html(html_message)


if __name__ == "__main__":
    app.run(host="192.168.2.115", port=888, auto_reload=True)
#访问地址http://localhost:端口号/life

# zsn888.github.io
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
def home(request):
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
    <body>  
        <p style="color: pink">郑淑宁专属抽签抢先版</p>  
         <!-- 图片展示 -->   
        <img src="/path/to/your/image/888.jpg" alt="示例图片" style="width:300px;height:auto;">
        <!-- 图片展示 -->  
        <img src="file:///E:/prometheus监控需要包/win/算卦/图片/888.jpg" alt="示例图片" style="width:300px;height:auto;">
        
        <h4>{word}</h4>  
        <p>抽到的卦为：{table.row_values(number)[0]}</p>  
        <p>卦名：{table.row_values(number)[1]}</p>  
        <p>解卦：{table.row_values(number)[3][3:50]}</p>  
        <p>      {table.row_values(number)[3][50:]}</p>  

        <!-- 抽签按钮 -->  
        <form action="/better" method="get">  
            <input type="submit" value="再抽一次">  
        </form> 

        <!-- 用户填写模块 -->  
        <form action="/submit" method="post">  
            <label for="user_input">希望添加好玩的建议：</label><br>  
            <input type="text" id="user_input" name="user_input" required><br><br>  
            <input type="submit" value="提交">  
        </form>  

        <!-- 图片展示 -->  
        <img src="E:\prometheus监控需要包\win\算卦\图片" style="width:300px;height:auto;">  

        <p style="color: pink">仅供娱乐。</p>  
    </body>  
    """
    return response.html(html_message)


@app.post('/submit')
async def submit(request):
    user_input = request.form.get('user_input', '')
    return response.html(f"<h4>您输入的内容是：{user_input}</h4>")


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

        <!-- 用户填写模块 -->  
        <form action="/submit" method="post">  
            <label for="user_input">希望添加好玩的建议：</label><br>  
            <input type="text" id="user_input" name="user_input" required><br><br>  
            <input type="submit" value="提交">  
        </form>  
        
        <!-- 抽签按钮 -->  
        <form action="/better" method="get">  
            <input type="submit" value="再抽一次">  
        </form> 
        
        <!-- 图片展示 -->  
        <img src="path_to_your_image.jpg" alt="示例图片" style="width:300px;height:auto;">  

        <p style="color: red">郑淑宁专属。</p>  
    </body>  
    """
    return response.html(html_message)


if __name__ == "__main__":
    app.run(host="192.168.2.115", port=888, auto_reload=True)

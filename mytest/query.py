# # 连接数据库
# import pymysql
 
# def getcontent():
#     db = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='demo',charset='utf8')
#     cursor = db.cursor()
#     sql = 'select * from username;'
#     cursor.execute(sql)
#     usercontent = cursor.fetchall()
#     print(usercontent)
#     for row in usercontent:
#         fname = row[0]
#         femail = row[1]
#         fpw = row[2]
#         ftime = row[3]
#         print('name=%s,email=%s,password=%s,createtime=%s' %(fname, femail, fpw,ftime))
#     db.close()
 
# if __name__ == '__main__':
#     getcontent()

# # 筛选某一条数据

# import pymysql
# import json
# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# from flask import Flask,request
# # from flask_cors import *
# app = Flask(__name__)
 
# @app.route('/index1', methods=['POST'])
# def zlindex():
#     inputData = request.json.get('username')
#     userdata = getcontent(inputData)
#     return userdata
 
# def getcontent(inputData):
#     db = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='demo',charset='utf8')
#     cursor = db.cursor()
#     sql = "select * from username where name = '%s';" %(inputData)      #username指表名  name指其中列名 demo指数据库
#     cursor.execute(sql)
#     usercontent = cursor.fetchall()
#     print(usercontent)
#     userjson = []
#     for row in usercontent:
#         fname = row[0]
#         femail = row[1]
#         fpw = row[2]
#         ftime = row[3]
#         # print('name=%s,email=%s,password=%s,createtime=%s' %(fname, femail, fpw,ftime))
#         user = 'name=%s,email=%s,password=%s,createtime=%s' %(fname, femail, fpw,ftime)
#         userjson.append(user)
#     db.close()
#     return json.dumps(userjson, ensure_ascii=False, indent=4)
 
# if __name__ == '__main__':
#     # getcontent()
#     app.run(host='0.0.0.0', port=5590)

# #post 或 get 获取数据

# import pymysql
# import json
# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
# from flask import Flask,request
# # from flask_cors import *
# app = Flask(__name__)
 
#  #Post请求(get直接换成get就行了)：
# @app.route('/index1', methods=['get'])
# def getcontent():
#     db = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='demo',charset='utf8')
#     cursor = db.cursor()
#     sql = 'select * from username;'
#     cursor.execute(sql)
#     usercontent = cursor.fetchall()
#     print(usercontent)
#     userjson = []
#     for row in usercontent:
#         fname = row[0]
#         femail = row[1]
#         fpw = row[2]
#         ftime = row[3]
#         # print('name=%s,email=%s,password=%s,createtime=%s' %(fname, femail, fpw,ftime))
#         user = 'name=%s,email=%s,password=%s,createtime=%s' %(fname, femail, fpw,ftime)
#         userjson.append(user)
#     db.close()
#     return json.dumps(userjson, ensure_ascii=False, indent=4)
 
# if __name__ == '__main__':
#     # getcontent()
#     app.run(host='0.0.0.0', port=5590)

import pymysql
import json
import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
from flask import Flask,request
app = Flask(__name__)
 
 
@app.route('/index1', methods=['POST'])
# def zlindex():
#     inputData = request.json.get('username')
#     userdata = getcontent(inputData)
#     return userdata
 
def getcontent():
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='demo',charset='utf8')
    cursor = db.cursor()
    sql = "select * from username"
    cursor.execute(sql)
    usercontent = cursor.fetchall()
    print(usercontent)
    userjson = []
    for row in usercontent:
        user = {'name': row[0], 'email': row[1], 'password': row[2], 'createtime': row[3].strftime("%Y-%m-%d %H:%M:%S")}
        userjson.append(user)
    db.close()
    return json.dumps(userjson, ensure_ascii=False, indent=4)  # 返回一个字典格式
 
 
if __name__ == '__main__':
    # getcontent()
    app.run(host='0.0.0.0', port=5590)
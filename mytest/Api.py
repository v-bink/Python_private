# python 接口测试

# # get方法:
# import requests
# import unittest
# class TeiBa(unittest.TestCase):
#     def setUp(self):
#         # 测试的url
#         self.url = "https://tieba.baidu.com/f?"
#         # 需要的参数
#         self.params = {"kw": "lol", "fr": "search"}
#         #添加请求头，模拟浏览器访问
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
#         #发送get请求
#         self.r = requests.get(self.url, params=self.params, headers=self.headers)

#     #编写一个测试用例，判断请求是否成功，是否包含搜索关键字
#     def test_tieba(self):
#         print("开始测试百度贴吧搜索接口:")
#         respones = self.r.text
#         #断言状态码是否为200
#         self.assertEqual(self.r.status_code,200)
#         #判断返回内容是否包含搜索关键词
#         self.assertIn('lol',respones)
#         # print(self.r.status_code)
#         print("测试通过")

#     def tearDown(self):
#         print("一条用例执行完成！")

# if __name__=='__main__':
#     unittest.main()

# get方法二: 访问方法:http://127.0.0.1:5000/test_1.0?name=小明&age=20 不在后面添加?name=小明&age=20对应值会显示None

from flask import Flask,request
import json

app = Flask(__name__)

# 只接受get方法访问
@app.route("/test_1.0",methods=["GET"])
def check():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断输入参数是否为null
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict,ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    age = get_data.get('age')
    # 对参数进行操作
    return_dict['result'] = tt(name,age)

    return json.dumps(return_dict,ensure_ascii=False)

# 功能函数
def tt(name, age):
    result_str = "%s今年%s岁" % (name, age)
    return result_str
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

# # post方法:  
# import requests
# import unittest
# class TeiBa(unittest.TestCase):
#     def setUp(self):
#         # 测试的url
#         self.url = "http://www.iamtxt.com/e/member/login/log.html"
#         # 需要的参数
#         self.params = {"username": "*******", "password": "*******"}
#         #添加请求头，模拟浏览器访问
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
#         #发送get请求
#         self.r = requests.post(self.url, json=self.params, headers=self.headers)

#     #编写一个测试用例，判断请求是否成功，是否包含搜索关键字
#     def test_tieba(self):
#         print("开始测试登录接口:")
#         respones = self.r.text
#         # #断言状态码是否为200  #结果状态码不为200是跳过
#         self.assertEqual(self.r.status_code,200)
#         print("登录成功")

#     def tearDown(self):
#         print("一条用例执行完成！")

# if __name__=='__main__':
#     unittest.main()

# # post方法二: 使用api访问方法:http://127.0.0.1:5000/test_1.0
# from flask import Flask, request
# import json

# app = Flask(__name__)

# # 只接受POST方法访问
# @app.route("/test_1.0", methods=["POST"])
# def check():
#     # 默认返回内容
#     return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
#     # 判断传入的json数据是否为空
#     if request.get_data() is None:
#         return_dict['return_code'] = '5004'
#         return_dict['return_info'] = '请求参数为空'
#         return json.dumps(return_dict, ensure_ascii=False)
#     # 获取传入的参数
#     get_Data = request.get_data()
#     # 传入的参数为bytes类型，需要转化成json
#     get_Data = json.loads(get_Data)
#     name = get_Data.get('name')
#     age = get_Data.get('age')
#     sex = get_Data.get('sex')
#     # 对参数进行操作
#     return_dict['result'] = tt(name, age,sex)

#     return json.dumps(return_dict, ensure_ascii=False)

# # 功能函数
# def tt(name, age,sex):
#     result_str = "%s今年%s岁,%s" % (name, age,sex)
#     return result_str

# if __name__ == "__main__":
#     app.run(debug=False, host='0.0.0.0', port=5000)

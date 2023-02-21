import json  # 导入json模块

# 1.将列表与元组数据转成json数组
listNumbers = [1, 3, 5, 7, 9]  # 列表数据
tupleNumbers = [2, 4, 6, 8, 10]  # 元组数据
jsonData1 = json.dumps(listNumbers)  # 将列表数据转成json数据
jsonData2 = json.dumps(tupleNumbers)  # 将元组数据转成json数据
print(f'列表转json数组：{jsonData1}')
print(f'元组转json数组：{jsonData2}')
print(type(jsonData1))
print(type(jsonData2))
# 列表转json数组：[1, 3, 5, 7, 9]
# 元组转json数组：[2, 4, 6, 8, 10]
# <class 'str'>
# <class 'str'>

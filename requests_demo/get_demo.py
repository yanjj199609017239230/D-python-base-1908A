#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/10'
# 自动化get 方式
# 先创建一个项目，建一个Demo包，在建一个模块
# 在Terminal输入命令pip install requests导入requests 包
# 无数据
from urllib import request

import requests


def no_paramters():
    r = requests.get("http://qa.yansl.com:8080/prefrenceArea/listAll")
    print(r.text)
    # text代表响应正文中的所有数据，并且是字符串形式
    print("应正文中的数据（字符串格式):"+ r.text)
    print("应正文中的数据（字典格式):", r.json())
    print("响应正文中的数据（二进制格式）:",r.content)#没有进行转换
    print("应正文中的数据（响应状态码):", r.status_code)
    print("响应头中的数据:",r.headers)
    print("请求行（请求方法):", r.request.method)
    print("请求头）url):", r.request.url)
    print("请求头:",r.request.headers)
    print("请求正文:",r.request.body)

import requests
# 键值对
def jian_zhi_dui():
    da = {
        "adminId":86,
        "roleIds":[1,2,3,4,5,6,7,4,4]
    }
    # post请求传键值对数据，用data，参数类型：dict
    r = requests.post("http://qa.yansl.com:8080/admin/role/update",data=da)
    print(r.text)

def uplode_file():
    data = {
        "pwd": "tr45rt344",
        "userName": "ing324df"
    }
    r = requests.post("http://api.yansl.com:8084/login",json=data)
    token = r.json()["data"]["token"]
    file = {'file':open(("sku.xls"),'rb')}
    print(file)
    header = {'token':token,'charset':'UTF-8'}
    r1 = requests.post("http://api.yansl.com:8084/product/uploaProdRepertory",files=file,headers=header)
    print(r1.text)

# 下载文件
def downlode_file():
    data = {
        "pwd": "tr45rt344",
        "userName": "ing324df"
    }
    r = requests.post("http://api.yansl.com:8084/login",json=data)
    print(r.text)
    token = r.json()["data"]["token"]
    header = {'token':token,'charset':'UTF-8'}
    r = requests.get("http://api.yansl.com:8084/product/downRepertoryTemplate",headers = header)
    conetent=r.content

    with open('dvd.xls','wb') as f:
        f.write(conetent)


if __name__ == '__main__':
    downlode_file()









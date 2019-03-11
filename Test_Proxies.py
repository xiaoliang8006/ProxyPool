# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:27:01 2019

@author: Administrator
"""
import requests

#获取代理
def get_proxy():
    try:
        response = requests.get('http://localhost:5000/get')
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return 0

#使用代理获取url内容
def  get_url_context(url):
    proxy = get_proxy()
    print("代理:",proxy)
    # 根据协议类型，选择不同的代理
    proxies = {
      "http": proxy,
      "https": proxy,
    }
    response = requests.get(url, proxies = proxies)
    response.encoding = "utf-8" #手动指定字符编码
    print(response.text)
    
    
get_url_context("http://zhangkeai.ml")




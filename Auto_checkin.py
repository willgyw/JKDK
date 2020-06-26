# -*- coding: utf-8 -*-
'''
@Author: Guo Yingwei
@Date: 2020-06-23 20:58:05
@E-mail: willgyw@126.com
@Description:  
@LastEditors: gyw
@LastEditTime: 2020-06-23 21:14:49
'''

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time


if __name__ == '__main__':
    #这里改成你的统一认证用户名和密码
    user_name = '2019050437'
    pwd = '000000'

    # 加上这两句话不打开浏览器
    option = webdriver.ChromeOptions()
    option.add_argument('headless') # 设置option
    # 用浏览器打开打卡的网址
    browser = webdriver.Chrome(options=option)
    browser.get('https://app.nwafu.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.nwafu.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex')

    # 输用户名和密码
    user_name_input = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input')
    user_name_input.send_keys(user_name)
    user_pwd_input = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input')
    user_pwd_input.send_keys(pwd)

    login_button = browser.find_element_by_xpath('//*[@id="app"]/div[3]')
    ActionChains(browser).move_to_element(login_button).click(login_button).perform()
    print('正在登陆')
    time.sleep(2)
    browser.get('https://app.nwafu.edu.cn/ncov/wap/default/index')

    # 获取位置
    wz = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[6]/div/input')
    ActionChains(browser).move_to_element(wz).click(wz).perform()
    print(wz.text)
    time.sleep(2)
    # 提交
    #tpost = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a')
    #ActionChains(browser).move_to_element(tpost).click(tpost).perform()

    # affirm
    #try:
        #affirm = browser.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]')
        #ActionChains(browser).move_to_element(affirm).click(affirm).perform()
        #print('打卡成功')
    #except:
        #ok = browser.find_element_by_xpath('//*[@id="wapat"]/div/div[2]/div')
        #ActionChains(browser).move_to_element(ok).click(ok).perform()
        #print('你今天已经打过卡了')
    time.sleep(2)
    #关闭浏览器
    browser.quit()


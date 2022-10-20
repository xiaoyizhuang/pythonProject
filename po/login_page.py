'''
对象层，调用基础层
'''
from selenium.webdriver.common.by import By

from base.basepage import Basepage


class loginPage(Basepage):

    #页面元素
    denglu01= (By.XPATH, '//*[@id="cloudHeader"]/div[1]/div[2]/div[5]/div/div[1]')#点击登录
    denglu02= (By.ID, 'tab-account')
    Username=(By.XPATH, '//*[@id="pane-account"]/div/form/div[1]/div/div/input')#账号
    Password=(By.XPATH, '//*[@id="pane-account"]/div/form/div[2]/div/div[1]/input')#密码
    denglu03=(By.XPATH, '//*[@id="pane-account"]/div/form/label/span[1]/span')#点击我同意
    denglu04=(By.XPATH, '//*[@id="pane-account"]/div/form/button')#登录
    #页面动作
    def login_ecshop(self):
        self.locator_element(loginPage.denglu01)
        self.locator_element(loginPage.denglu02)
        self.locator_element(loginPage.Username).send_keys('asiaInfo_ceshi_huangrenzheng')
        self.locator_element(loginPage.Password).send_keys('taiaTP68')
        self.locator_element(loginPage.denglu03)
        self.locator_element(loginPage.denglu04)
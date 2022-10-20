"""
基础层
"""
import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class Basepage:
    def __init__(self):

        # global webdriver
        self.driver = webdriver.Chrome()
        self.driver.get('https://ecloud.10086.cn:31015//')
        # time.sleep(3)  # 休眠3秒

        self.driver.maximize_window()  # 浏览器最大化
        self.driver.find_element_by_id('bottom_space').send_keys('G2Bent')
        self.driver.find_element(By.XPATH, '//*[@id="cloudHeader"]/div[1]/div[2]/div[5]/div/div[1]').click()  # 点击登录
        time.sleep(3)
        self.driver.find_element(By.ID, 'tab-account').click()
        self.driver.find_element(By.XPATH, '//*[@id="pane-account"]/div/form/div[1]/div/div/input').send_keys(
            'asiaInfo_ceshi_huangrenzheng')  # 登录账号
        self.driver.find_element(By.XPATH, '//*[@id="pane-account"]/div/form/div[2]/div/div[1]/input').send_keys(
            'taiaTP68')  # 登录密码
        self.driver.find_element(By.XPATH, '//*[@id="pane-account"]/div/form/label/span[1]/span').click()  # 点击我同意
        self.driver.find_element(By.XPATH, '//*[@id="pane-account"]/div/form/button').click()  # 点击登录
        # time.sleep(3)

    def locator_element(self, loc: object) -> object:
        return self.driver.find_element(*loc)


import select
from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import select


class Testcase(unittest.TestCase):

    def test_01_login(self):
        '''
        订购云主机
        :return:
        '''
        driver = webdriver.Chrome()
        driver.get('https://ecloud.10086.cn:31015//')
        time.sleep(3) #休眠3秒

        driver.maximize_window()#浏览器最大化
        # driver.find_element_by_id('bottom_space').send_keys('G2Bent')
        driver.find_element(By.XPATH,'//*[@id="cloudHeader"]/div[1]/div[2]/div[5]/div/div[1]').click()#点击登录
        time.sleep(3)
        driver.find_element(By.ID,'tab-account').click()

        driver.find_element(By.XPATH,'//*[@id="pane-account"]/div/form/div[1]/div/div/input').send_keys('asiaInfo_ceshi_huangrenzheng')#登录账号
        driver.find_element(By.XPATH,'//*[@id="pane-account"]/div/form/div[2]/div/div[1]/input').send_keys('taiaTP68')#登录密码
        driver.find_element(By.XPATH,'//*[@id="pane-account"]/div/form/label/span[1]/span').click()#点击我同意
        driver.find_element(By.XPATH,'//*[@id="pane-account"]/div/form/button').click()#点击登录
        time.sleep(3)
        """查询商品"""
        xuanfu = driver.find_element(By.XPATH,'//*[@id="cloudHeader"]/div[1]/div[1]/div[3]')#鼠标悬浮在产品
        ActionChains(driver).move_to_element(xuanfu).perform()#悬浮
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="cloudHeader"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/ul/li[1]/span[2]/span[1]').click()
        #点击云主机
        driver.find_element(By.XPATH,'//*[@id="product-banner"]/div/div[2]/div[2]/div[3]/a').click()
        #点击订购
        handles =  driver.window_handles
        for handle in handles:
             if handle != driver.current_window_handle:
                  driver.switch_to.window(handle)
             handle = driver.window_handles
        print("所有窗口的句柄{}".format(handle))
        driver.switch_to.window(handle[-1])
        print("当前窗口句柄{}".format(driver.current_window_handle))
        #切换窗口
        time.sleep(20)


        driver.find_element(By.XPATH,'//*[@id="app"]/section/div/div[3]/ul/li/ul/li[1]/span').click()

        #跳转框架
        # driver.switch_to.frame('框架名字')
        # select（导包alt+回车）#用于下拉框选择
        # select.select_by_value("值")
        #处理弹窗：alert（只有确定），confirm（有确定，有取消），prompt（有确定，有取消，还可以输入值）
        # ale=driver.switch_to.alert
        # ale.accept()#accept点击确定，dismiss点击取消，text获得文本，send_kes输入值

# if __name__ == '__main__':
#     unittest.main()
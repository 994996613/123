#coding=utf-8

import unittest
import time
from selenium import webdriver




class login(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
         
       
    def testName(self):
        
        self.driver.get('http://newtours.demoaut.com/')
        self.driver.find_element_by_name('userName').send_keys('mecury')
        self.driver.find_element_by_name('password').send_keys('mecury')
        self.driver.find_element_by_name('login').click()
        time.sleep(5)
    

    #def tearDown(self):
       # self.driver.close()


if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
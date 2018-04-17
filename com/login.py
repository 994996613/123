# coding=utf-8

from selenium import webdriver
import unittest
import time
driver = webdriver.Firefox()
#��URL
driver.get('http://newtours.demoaut.com/')
#��ͼ
#������־
#��xxx���������xxx����
driver.find_element_by_name('userName').send_keys('mecury')
driver.find_element_by_name('password').send_keys('mecury')
#��ͼ
#������־
#���xxx��ť
driver.find_element_by_name('login').click()
time.sleep(5)
#��ͼ
#������־
#Ԥ�ڽ��


driver.close()
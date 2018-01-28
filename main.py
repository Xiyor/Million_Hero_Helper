import time
time_s = time.time()

#coding:utf-8
from Million_Hero_Helper.ocr_api import baidu_ocr_api
from Million_Hero_Helper.simulator_screenshot import screenshot_obtain
from Million_Hero_Helper.start_web_search import start_search

app_label = "Qt5QWindowIcon"
screenshot_obtain(app_label)
content = baidu_ocr_api()
start_search(content)
time_e = time.time()
print("time cost: {}".format(time_e - time_s))
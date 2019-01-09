#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-12-26 10:57
# @Author   : Hhh
# @File     ：get_crb_img.py

import csv
import operator as op
import time
import threading
import requests
import os

file_path = './docs/dr/135_'
local_path = 'd:/dataset/kaggle/crb/'
url = 'http://www.wjlpt.com:8080/test'
threads = []



def download_crb_img(checkup_time, img_path, img_name, org_id, file_id):
   try:
       img = url + img_path + '/' + img_name
       r = requests.get(img)
       s = requests.session()
       s.keep_alive = False
       # 拼接成 orgid_DABH.jpg形式
       save_path = local_path + str(checkup_time) + '/' + str(file_id) + '/'
       save_file = save_path + org_id + '_' + img_name
       print(save_file)
       isExists = os.path.exists(save_path)
       if not isExists:
           os.makedirs(save_path)
       with open(save_file, "wb") as code:
           code.write(r.content)
   except:
       print("停5秒")
       time.sleep(5)


def read_csv_img(fname,file_id):
    with open(fname) as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if (i > 0):  # 第一行从0开始
                if (op.eq(row[0], '{}') != True):
                    org_id = row[0]
                    img_path = row[1]
                    img_name = row[2]
                    print("下载" + img_name)
                    # 如果是1开头
                    if img_name.startswith('1'):
                        pass
                        #download_crb_img(1, img_path, img_name, org_id, file_id)
                    # 如果是3开头
                    elif img_name.startswith('3'):
                        pass
                        #download_crb_img(3, img_path, img_name, org_id, file_id)
                    # 如果是4开头
                    else:
                        download_crb_img(4, img_path, img_name, org_id, file_id)
            else:
                continue
for j in range(1, 14):
    fname = file_path + str(j) + '.csv'
    t = threading.Thread(target=read_csv_img, name="Thread-{}".format(j), args=(fname,j))
    t.start()
    print('线程启动' + fname)
# if __name__ == '__main__':
#     for t in threads:
#         t.setDaemon(True)


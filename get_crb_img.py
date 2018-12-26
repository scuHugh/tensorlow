#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-12-26 10:57
# @Author   : Hhh
# @File     ：get_crb_img.py

import csv
import operator as op
import time
from time import sleep
import threading

import requests
import os

file_path = './docs/'
local_path = 'd:/dataset/kaggle/crb/'
url = 'http://www.wjlpt.com:8080/test'
threads = []


def download_crb_img(checkup_time, img_path, img_name, org_id, file_id):
    img = url + img_path + '/' + img_name
    r = requests.get(img)
    s = requests.session()
    # 拼接成 orgid_DABH.jpg形式
    save_path = local_path + str(checkup_time) + '/' + str(file_id) + '/'
    save_file = save_path + org_id + '_' + img_name
    print(save_file)
    isExists = os.path.exists(save_path)
    if not isExists:
        os.makedirs(save_path)
    with open(save_file, "wb") as code:
        code.write(r.content)
    s.keep_alive = False


def read_csv_img(fname):
    print('线程启动' + fname)
    with open(fname) as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            count = 1
            file_id = 0
            if (i > 0):  # 第一行从0开始
                if count % 10000 == 0:
                    file_id = file_id + 1
                if (op.eq(row[0], '{}') != True):
                    count = count + 1
                    org_id = row[0]
                    img_path = row[1]
                    img_name = row[2]
                    print("下载" + img_name)
                    # 如果是1开头
                    if img_name.startswith('1'):
                        download_crb_img(1, img_path, img_name, org_id, file_id)
                    # 如果是3开头
                    elif img_name.startswith('3'):
                        download_crb_img(3, img_path, img_name, org_id, file_id)
                    # 如果是4开头
                    else:
                        download_crb_img(4, img_path, img_name, org_id, file_id)
            else:
                pass


for j in range(0, 10):
    fname = file_path + str(j) + '.csv'
    print(fname)
    t = threading.Thread(target=read_csv_img, name="Thread-{}".format(j), args=(fname,))
    threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
        sleep(0.1)

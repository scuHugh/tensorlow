#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-12-26 16:37
# @Author   : Hhh
# @File     ：cut_csv.py
import csv
import os

path = './docs/dr/135dr.csv'

with open(path) as file:
    csvreader = csv.reader(file)
    a = next(csvreader)
    i = j = 1
    for row in csvreader:
        # 每50000个就j加1， 然后就有一个新的文件名
        if i % 10000 == 0:
            j += 1
            print("生成"+str(j)+".csv")
        csv_path = './docs/dr/135_'+str(j) + '.csv'
        if not os.path.exists(csv_path):
            with open(csv_path, 'w', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(row)
            i += 1
        # 存在的时候就往里面添加
        else:
            with open(csv_path, 'a', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(row)
            i += 1

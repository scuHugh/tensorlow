#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-12-25 11:51
# @Author   : Hhh
# @File     ：mysql_to_csv.py
import csv

f = open('./docs/dr/135dr.txt', encoding="UTF-8")
with open('./docs/135dr.csv', "w", newline='') as fout:
  writer = csv.writer(fout)
  for line in f.readlines():
        t=line.strip().split('\t')
        print(t)
        writer.writerows([t])
  fout.close()
f.close()


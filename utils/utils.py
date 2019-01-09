#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-11-30 11:43
# @Author   : Hhh
# @File     ：utils.py
import json
import operator as op
import os, random, cv2
import csv

class Utils():
    def __init__(self):
        self.data_path = 'd:/dataset/dog/'
        self.source_path = 'd:/dataset/dog/'

    def set_label(self):
        # 获得标签
        path = self.data_path
        imgs = os.listdir(path)
        count = 1
        for i in imgs:
            oldName = path + i
            newName = path + str(count) + '.jpg'
            os.rename(oldName,newName)
            count=count+1
        print(imgs)
    def read_csv(self):
        filename = self.source_path + 'test_1.csv'
        csv_file = open(self.source_path + 'train1.csv', 'w', newline='')
        csv_header = ['filename','width','height','class','xmin','ymin','xmax','ymax']
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(csv_header)
        with open(filename) as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
             if i > 0:  # 第一行从0开始
                newRow = []
                if(op.eq(row[6],'{}') != True):
                    print(row)
                    fname = row[0]
                    label = 'bixiong'
                    width = json.loads(row[3])['width']
                    height = json.loads(row[3])['height']
                    xmin = json.loads(row[6])['x']
                    ymin = json.loads(row[6])['y']
                    xmax = json.loads(row[6])['x'] + json.loads(row[6])['width']
                    ymax = json.loads(row[6])['y'] + json.loads(row[6])['height']
                    newRow = [fname,width,height,label,xmin,ymin,xmax,ymax]
                    csv_writer.writerow(newRow)
        csv_file.close()
        f.close()






if __name__ == '__main__':
    ut = Utils()
    # ut.set_label()
    ut.read_csv()
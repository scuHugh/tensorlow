#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-12-12 18:56
# @Author   : Hhh
# @File     ：Flask_api.py
from flask import Flask, request, json, jsonify
from ObjectDetection import detect_jpg
import os

app = Flask(__name__)

# jpg识别
@app.route('/check')
def index():
    if request.method == 'GET':
       pic_path=request.args.get('data')
       os.rename(pic_path, pic_path + ".jpg")
       pic_path = pic_path + ".jpg"
       x1,x2,y1,y2,class_name,result=detect_jpg.get_results(pic_path)
       if(len(result)>0):
           respose = {
               'data': json.dumps(result),
               'status': 4
           }
           return jsonify(respose)
       else:
         return jsonify({'status': 8, 'data': '无结果'})
    else:
       pass

if __name__ =="__main__":
    app.run()
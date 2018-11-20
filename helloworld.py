#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-11-20 11:18
# @Author   : Hhh
# @File     ：helloworld.py

import tensorflow as tf
import numpy as np
import pickle

tensor = [1,2,3,4,5,6]
A = [[1,2,3,4,6,5]]
B = [[[1,3],
     [6,4],
     [9,6]],
    [[66,55],
     [88,77],
     [99,66]],
     ]
test_num = 2

print(tensor[:test_num])  # 读到第test_num个 [1,2]
print(tensor[test_num:])  # 读前test_num个 [3,4,5,6]

batch_x = np.zeros([10, 2 * 1])
print(batch_x[1,:])  #batch_x中第一个元素
sess = tf.Session()
#
print('Ashape:',tf.shape(A),sess.run(tf.argmax(A,1))) # 返回最大的那个数值所在的下标,0是看y轴,1是看x轴
print('Bshape:',tf.shape(B),sess.run(tf.argmax(B,2))) #


def load_file(filename):
    with open(filename, 'rb') as fo:
        data = pickle.load(fo, encoding='latin1')
    return data

data = load_file('d:/dataset/cifar-10/test_batch')
print(data.keys())
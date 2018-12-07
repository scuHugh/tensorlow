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

# reshape
a = np.zeros((10,2))
print(a.T)
print(np.reshape(a,(a.shape[0],-1)))

# np.dot
# 矩阵乘法
a = np.array([[1,2,3],[4,5,6]]) # 2*3
b = np.array([[1,2],[3,4],[5,6]]) # 3*2
dot1 = np.dot(a,b) #  [[22 28],[49 64]] 2*2
dot2 = np.dot(b,a) # [[ 9 12 15],[19 26 33],[29 40 51]] 3*3
dot3 = b@a # [[ 9 12 15],[19 26 33],[29 40 51]] 3*3
# dot4 = np.multiply(a,b) #error
print("dot1 %s" %(dot1))
print("dot2 %s" %(dot2))
print("dot3 %s" %(dot3))


# np.multiply
# 对应元素相乘

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [4, 7, 1]])
print(a*b)  # [[ 7 16 27], [16 35  6]]
print(np.multiply(a,b)) # [[ 7 16 27], [16 35  6]]

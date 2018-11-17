#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-11-17 11:32
# @Author   : Hhh
# @File     ：Load.py
import tensorflow as tf
import numpy as np
# 定义与保存的参数相同的size才能导入
W = tf.Variable(np.arange(6).reshape((2,3)),dtype=tf.float32,name='weights')
b = tf.Variable(np.arange(3).reshape((1,3)),dtype=tf.float32,name='b')

# restore 不用定义init

saver = tf.train.Saver()
sess = tf.Session()
saver.restore(sess,'./data/save.ckpt')
print("Weight",sess.run(W))
print("b",sess.run(b))


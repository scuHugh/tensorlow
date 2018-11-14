#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-11-08 19:04
# @Author   : Hhh
# @File     ：tf_build_network.py
from __future__ import print_function
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, activation_function=None):
    # 添加层数并且返回这层的output
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
           weights = tf.Variable(tf.random_normal([in_size, out_size]),name='W')
        with tf.name_scope('biase'):
           biases = tf.Variable(tf.zeros([1, out_size]) + 0.1,name='b')
        with tf.name_scope('Wx_plus_b'):
           Wx_plus_b = tf.matmul(inputs, weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

# 构造数据
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) + 3.4 + noise

# 定义网络的输入

with tf.name_scope('input'):
  xs = tf.placeholder(tf.float32, [None, 1],name='x_input')
  ys = tf.placeholder(tf.float32, [None, 1],name='y_input')
# 添加隐藏层
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# 添加输出层
prediction = add_layer(l1, 10, 1, activation_function=None)
# loss
with tf.name_scope('loss'):
   loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]),name='loss')
with tf.name_scope('train'):
   train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
writer = tf.summary.FileWriter("./logs",sess.graph)
# activate tensorflow 后到logs
# 上一级 tensorboard --logdir=logs
# 多一个空格也不行
sess.run(init)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data,y_data)
# show了不暂停
plt.ion()
plt.show()

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))
        try:
          ax.lines.remove(lines[0])
        except Exception:
          pass
        prediction_value = sess.run(prediction,feed_dict={xs:x_data})
        lines = ax.plot(x_data,prediction_value,'r-',lw=5)
        plt.pause(0.5)


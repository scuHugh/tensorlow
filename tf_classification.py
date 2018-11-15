#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-11-15 15:30
# @Author   : Hhh
# @File     ：tf_classification.py
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets('D:\dataset\MNIST_data',one_hot=True)


def nn_layer(inputs, in_size, out_size,activation_function=None):
    # 添加层数并且返回这层的output
     weights = tf.Variable(tf.random_normal([in_size, out_size]))
     biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
     Wx_plus_b = tf.matmul(inputs, weights) + biases
     if activation_function is None:
            outputs = Wx_plus_b
     else:
            outputs = activation_function(Wx_plus_b)
     return outputs
def computr_accuracy(v_xs,v_ys):
    global prediction
    y_pre = sess.run(prediction,feed_dict={xs:v_xs})
    correct_prediction = tf.equal(tf.argmax(y_pre,1),tf.argmax(v_ys,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    result = sess.run(accuracy,feed_dict={xs:v_xs,ys:v_ys})
    return result
# defined placeholder for inputs to network
xs = tf.placeholder(tf.float32,[None,784]) # 28*28
ys = tf.placeholder(tf.float32,[None,10])

#  add output layer
prediction = nn_layer(xs,784,10,activation_function=tf.nn.softmax)

# the error between prediction and real data
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys*tf.log(prediction),
                                              reduction_indices=[1]))  #loss 交叉熵
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(1001):
    batch_xs,batch_ys = mnist.train.next_batch(200) #每次提取200个学习
    sess.run(train_step,feed_dict={xs:batch_xs,ys:batch_ys})
    if i%50 == 0:
        print('步数',i,computr_accuracy(
            mnist.test.images,mnist.test.labels))



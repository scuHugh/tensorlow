#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-11-17 11:23
# @Author   : Hhh
# @File     ：Saver.py
import tensorflow as tf

# Saver
W = tf.Variable([[1,2,3],[4,5,6]],dtype=tf.float32,name='weights')
b = tf.Variable([[1,2,3]],dtype=tf.float32,name='b')
init = tf.initialize_all_variables()

saver = tf.train.Saver()

sess = tf.Session()
sess.run(init)

save_path = saver.save(sess,'./data/save.ckpt')
print('Save to path:',save_path)
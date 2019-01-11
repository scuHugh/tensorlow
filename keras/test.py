#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2019-01-09 11:28
# @Author   : Hhh
# @File     ：test.py
import keras
from keras.models import Sequential,Model,load_model
from keras.layers import Dense,Activation,Conv2D,MaxPool2D,Flatten,Dropout,Input
import numpy as np
#
# # 卷积层
# model.add(Conv2D(64,(3,3),activation='relu',input_shape=(224,224,32)))
# # 池化层
# model.add(MaxPool2D(pool_size=(2,2)))
# #  全连接层
# model.add(Dense(256,activation='relu'))
# # Dropout
# model.add(Dropout(0.5))
# # flatten
# model.add(Flatten())
# # loss 和optimizer
# model.compile(loss='binary_crossentropy',optimizer='rmsprop')
# # 输入数据
# model.fit(x_train, y_train, batch_size = 32, epochs = 10, validation_data(x_val, y_val))
# # 测试
# score = model.evaluate(x_test,y_test,batch_size=32)
#
trX = np.linspace(-1,1,101)
trY = 3 * trX + np.random.randn(*trX.shape) * 0.33

model = Sequential()
model.add(Dense(input_dim=1,output_dim=1,init='uniform',activation='linear'))

model.load_weights('test.h5')

weights = model.layers[0].get_weights()
w_init = weights[0][0][0]
b_init = weights[1][0]
print('Linear regression model is initialized with weights w: %.2f,b: %2f' % (w_init,b_init))
model.compile(optimizer='sgd',loss='mse')

model.fit(trX,trY,nb_epoch=100,verbose=1)

weights = model.layers[0].get_weights()
w_final = weights[0][0][0]
b_final = weights[1][0]
print('Linear regression model is trained to have weight w: %.2f, b: %.2f' % (w_final, b_final))

#model.save_weights('test.h5')
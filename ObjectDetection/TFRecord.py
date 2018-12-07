#!/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 2018-11-30 13:54
# @Author   : Hhh
# @File     ：TFRecord.py
"""
Usage:
python TFRecord.py --csv_input=d:/dataset/dog/train.csv --image_dir=d:/dataset/dog/bixiong
--output_path=d:/dataset/dog/train.record
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
import tensorflow as tf

from PIL import Image
# from object_detection.utils import dataset_util
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
FLAGS = flags.FLAGS


# 将分类名称转成ID号
def class_text_to_int(row_label):
    if row_label == 'bixiong':
        return 1
    # elif row_label == 'car':
    #     return 2
    # elif row_label == 'person':
    #     return 3
    # elif row_label == 'kite':
    #     return 4
    else:
        print('NONE: ' + row_label)
        # None


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    print(os.path.join(path, '{}'.format(group.filename)))
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read() #读取结果是最原始的图像
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height= image.size
    format = image.format
    if format == 'JPEG' or format == 'PNG':
        filename = (group.filename).encode('utf8')
        image_format = b'jpg'
        xmins = []
        xmaxs = []
        ymins = []
        ymaxs = []
        classes_text = []
        classes = []

        for index, row in group.object.iterrows():
            xmins.append(row['xmin'] / width)
            xmaxs.append(row['xmax'] / width)
            ymins.append(row['ymin'] / height)
            ymaxs.append(row['ymax'] / height)
            classes_text.append(row['class'].encode('utf8'))
            classes.append(class_text_to_int(row['class']))

        tf_example = tf.train.Example(features=tf.train.Features(feature={
            'image/height': dataset_util.int64_feature(height),
            'image/width': dataset_util.int64_feature(width),
            'image/filename': dataset_util.bytes_feature(filename),
            'image/source_id': dataset_util.bytes_feature(filename),
            'image/encoded': dataset_util.bytes_feature(encoded_jpg),
            'image/format': dataset_util.bytes_feature(image_format),
            'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
            'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
            'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
            'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
            'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
            'image/object/class/label': dataset_util.int64_list_feature(classes),
        }))
    else:
        return 0
    return tf_example


def main(csv_input, output_path, imgPath):
    writer = tf.python_io.TFRecordWriter(output_path)
    path = imgPath
    examples = pd.read_csv(csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        if(tf_example):
           writer.write(tf_example.SerializeToString())
        else:
            print(group.filename, "不是jpg或png", )
    writer.close()
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    # imgPath = 'E:\data\Images'
    imgTrain = r'd:/dataset/dog/train'
    imgVal = r'd:/dataset/dog/val'

    # 生成train.record文件
    output_path = 'd:/dataset/dog/train.record'
    csv_input = 'd:/dataset/dog/train.csv'
    main(csv_input, output_path, imgTrain)

    # 生成验证文件 val.record
    output_path = 'd:/dataset/dog/val.record'
    csv_input = 'd:/dataset/dog/val.csv'
    main(csv_input, output_path, imgVal)


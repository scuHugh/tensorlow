import csv
import json
import os
import operator as op
import time

path = 'D:/dataset/crb/'
predict_path = 'D:/dataset/crb/predict'
header = ['filename','uid','file_size','file_attributes','region_count','region_id','region_shape_attributes','region_attributes']

def predict_by_csvfile(filename):
    print("正在处理"+filename+':')
    start = time.time()
    with open(path+filename, encoding='UTF-8') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if (i > 0):  # 第一行从0开始
                if (op.eq(row[0], '{}') != True):
                    # 存到org_id文件夹的csv文件中
                    img_id, score, x, y, w, h = row
                    org_id, dabh = img_id.split('_', 1)
                    region_shape_attributes = {
                        "name": "rect",
                        "x": x,
                        "y": y,
                        "width": w,
                        "height": h
                    }
                    region_attributes = {
                        "label": "AI"
                    }
                    newRow = [dabh, '', -1, '', '', '', json.dumps(region_shape_attributes),
                              json.dumps(region_attributes)]
                    predict_file = predict_path + '/' + org_id + '.csv'
                    if not os.path.exists(predict_file):
                        with open(predict_file, 'w', newline='') as file:
                            csvwriter = csv.writer(file)
                            csvwriter.writerow(header)
                            csvwriter.writerow(newRow)
                    # 存在的时候就往里面添加
                    else:
                        with open(predict_file, 'a', newline='') as file:
                            csvwriter = csv.writer(file)
                            csvwriter.writerow(newRow)
                else:
                    pass
    end = time.time()
    print(" 执行时间 = %f seconds"%(end-start))

if __name__ =="__main__":
    files = os.listdir(path)
    files_csv = list(filter(lambda x: x[-4:] == '.csv', files))
    for f in files_csv:
        predict_by_csvfile(f)


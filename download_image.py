# coding:utf-8
import os
import csv
import urllib.request

image_url = 'http://yun.tuitiger.com/mami-media/img/m0po2fr1lh.gif'
file_path = '/Users/mark1xie/workspace-html/images/'

img_list = []
f = csv.reader(open('/Users/mark1xie/workspace-html/image_csv/汇总结果-500.csv', 'r'))
for i in f:
    img_url = "http:" + ''.join(i)
    img_list.append(img_url)

print(img_list)

try:
    if not os.path.exists(file_path):
        os.makedirs(file_path)  # 如果没有这个path则直接创建
    file_suffix = os.path.splitext(image_url)[1]
    filename = '{}{}'.format(file_path, file_suffix)
    urllib.request.urlretrieve(image_url, filename=filename)

except IOError as e:
    print(1, e)

except Exception as e:
    print(2, e)

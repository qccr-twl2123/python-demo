# coding:utf-8
import os
import csv
import urllib.request
import requests


class DownloadImage(object):

    def __init__(self):
        pass

    def collection_images(self):
        img_list = []
        f = csv.reader(open('/Users/mark1xie/workspace-html/image_csv/汇总结果-500.csv', 'r'))
        for i in f:
            img_url = "http:" + ''.join(i)
            img_list.append(img_url)
        return img_list

    def download_url_file(self, image_url, file_path, file_name):
        data = requests.get(image_url).content
        with open(file_path + file_name, 'wb') as f:
            f.write(data)


if __name__ == '__main__':
    downloadImage = DownloadImage()
    img_list = downloadImage.collection_images();
    for img_url in img_list:
        downloadImage.download_url_file(img_url, "/Users/mark1xie/workspace-html/", os.path.basename(img_url))

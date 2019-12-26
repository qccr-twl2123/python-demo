# -*- coding: utf-8 -*-

import requests
import os

image_url = "http://yun.tuitiger.com/mami-media/img/m0po2fr1lh.gif"
data = requests.get(image_url).content
with open('/Users/mark1xie/workspace-html/m.jpg', 'wb') as f:
    f.write(data)


url = 'http://www.**.net/images/logo.gif'
filename = os.path.basename(url)
print(filename)


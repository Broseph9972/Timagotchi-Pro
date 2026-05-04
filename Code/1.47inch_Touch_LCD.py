#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import jd9853
import axs5106l
from PIL import Image,ImageDraw,ImageFont

if __name__=='__main__':
    
    disp = jd9853.jd9853()
    disp.clear()
    touch = axs5106l.axs5106l()
    

    logging.info("show image")
    # 定义图片文件夹路径
    pic_folder = "./pic/"

    # 初始化一个空列表来存储图片文件路径
    ImagePath = []

    # 遍历指定文件夹下的所有文件和文件夹
    for filename in os.listdir(pic_folder):
        # 拼接完整的文件路径
        file_path = os.path.join(pic_folder, filename)
        # 检查是否为文件以及文件扩展名是否为图片格式（这里以常见的.png为例）
        if os.path.isfile(file_path) and (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
            ImagePath.append(file_path)

    for i in range(0, 12):
        image = Image.open(ImagePath[i])	
        # image = image.rotate(0)
        disp.show_image(image)
        time.sleep(1)
    
    disp.clear()
    color = [0] * 2
    color[0] = 0x00fe
    color[1] = 0xfe00
    while True:
        touch.read_touch_data()
        point, coordinates = touch.get_touch_xy()
        if point != 0 and coordinates:
            for i in range(point):
                coordinates[i]['x'] = 171 - coordinates[i]['x']
                disp.dre_rectangle(
                    coordinates[i]['x'], coordinates[i]['y'],
                    coordinates[i]['x'] + 5, coordinates[i]['y'] + 5,
                    color[i]  # 矩形的颜色
                )
                print(f"point {i + 1} coordinates: x={coordinates[i]['x']}, y={coordinates[i]['y']}")
        time.sleep(0.01)

#!/usr/bin/env python
# coding: utf-8


import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import jieba
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import patches



def make_mask (shape, dpi) :
    mask_fig = plt.figure(figsize=(6,6),facecolor='w',dpi=dpi)
    mask_ax = mask_fig.add_subplot(111)
    xy_center = (0.5,0.5)
    if (shape == 'circle' or shape == 'c'):
        mask_ax.add_patch(patches.Circle(xy_center, 0.5))
    elif (shape == 'ellipse' or shape == 'e'):
        mask_ax.add_patch(patches.Ellipse(xy_center, 1, 0.75))
    elif (shape == 'rectangle' or shape == 'r'):
        mask_ax.add_patch(patches.Rectangle((0,0.15), 1, 0.7))
    elif (shape == 'square' or shape == 's'):
        mask_ax.add_patch(patches.Rectangle((0,0), 1, 1))
    else :
        shape = int(shape)
        mask_ax.add_patch(patches.RegularPolygon(xy_center, shape, 0.5))
    mask_ax.axis('off')
    mask_fig.savefig('mask.png')
    mask = np.array(Image.open('mask.png'))
    plt.close()
    return mask




def jieba_split (text_addr):
    text = open(text_addr).read()
    text_split = ' '.join(jieba.cut(text))
    return text_split




def cloud_generate (text_addr, shape, colormap, dpi = 200, output_addr = 'wordcloud_output.png'):
    my_wordcloud = WordCloud(height=(6*dpi), width=(6*dpi),
                             mask=make_mask(shape, dpi), font_path='simhei.ttf',
                             background_color='white').generate(jieba_split(text_addr))
    cloud_fig = plt.figure(figsize=(6,6), dpi=dpi)
    cloud_ax = cloud_fig.add_subplot(111)
    cloud_ax.imshow(my_wordcloud.recolor(colormap = colormap))
    cloud_ax.axis('off')
    cloud_fig.savefig('wordcloud_output.png')
    return




cloud_generate(text_addr='blog1.txt', shape = 'c', colormap='Set2', dpi=200)






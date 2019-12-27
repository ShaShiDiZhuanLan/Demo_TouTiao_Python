# coding: utf-8
"""
Author: 沙振宇
Update Time: 2019-12-26
Info: 词频分析
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image # pip install pillow
from wordcloud import WordCloud
import jieba

def word_count(path):
    txt = open(path, 'r', encoding='utf-8').read()

    words = jieba.lcut(txt)  # 精准切词
    count = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            count[word]=count.get(word, 0) + 1
    return count

def create_word_cloud(source, wordlist, filename):
    cloud_mask = np.array(Image.open(source))#词云的背景图，需要颜色区分度高

    wc = WordCloud(
        background_color="black",   #背景颜色
        mask=cloud_mask,            #背景图cloud_mask
        max_words=100,              #最大词语数目
        font_path='simsun.ttf',     #调用simsun.tff字体
        height=1200,                #设置高度
        width=1600,                 #设置宽度
        max_font_size=1000,         #最大字体号
        random_state=1000,          #设置随机生成状态，即有多少种配色方案
    )

    print("生成词云")
    my_word = wc.generate(wordlist)  # 用 word list 生成词云
    # 展示词云图
    plt.imshow(my_word)
    plt.axis("off")
    plt.show()
    wc.to_file(filename)  # 把词云保存下当前目录（与此py文件目录相同）

def main():
    count = word_count('data/all.txt')
    result = sorted(count.items(),key=lambda x:x[1],reverse=True)
    str_word_list = ""
    for i in range(2000):
        word, count = result[i]
        str_word_list = str_word_list + " " + word
        print(word, ':', count)

    print("开始创建词云")
    create_word_cloud("resource/bubble2.png", str_word_list, "效果2.png")
    # create_word_cloud("resource/monkey.jpg", str_word_list, "效果2.png")

if __name__ == '__main__':
    main()

#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->dataset_text
# @Time      :2022/9/24 21:30
# @Author    :Peng neng
# @File      :dataprocess_text.py
# ===============================
import jieba
path = "../data/weibo_text/weibo_senti_100k.csv"
data_list = data_path = open(path, encoding='utf-8').readlines()[1:]
path_stop_words = "../data/weibo_text/hit_stopword"
stop_words = open(path_stop_words, encoding='utf-8').readlines()[1:]
stop_word_List = [line.strip() for line in stop_words]
stop_word_List.append(" ")
stop_word_List.append("\n")

if __name__ == '__main__':
    voc_dict = {}
    min_seq = 1
    top_n = 1000
    UNK = "<UNK>"
    PAD = "<PAD>"
    for item in data_list:
        label = item[0]
        content = item[2:].strip()
        seg_list = jieba.cut(content, cut_all=False)
        seg_res = []
        for seg_item in seg_list:
            if seg_item in stop_word_List:
                continue
            seg_res.append(seg_item)
            if seg_item in voc_dict.keys():
                voc_dict[seg_item]  = voc_dict[seg_item] + 1
            else:
                voc_dict[seg_item] = 1

        print(content)
        print(seg_res)

    voc_list = sorted([_ for _ in voc_dict.items() if _[1] > min_seq],
                      key=lambda x : x[1],
                      reverse=True)[:top_n]

    voc_dict = {word_count[0]: idx for idx, word_count in enumerate(voc_list)}

    voc_dict.update({UNK: len(voc_dict), PAD: len(voc_dict) + 1})

    # print(voc_dict)

    ff = open("../data/weibo_text/dict", "w", encoding="utf-8")
    for item in voc_dict.keys():
        ff.write("{}, {}\n".format(item, voc_dict[item]))





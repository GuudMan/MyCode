#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->dataset_text
# @Time      :2022/9/24 23:03
# @Author    :Peng neng
# @File      :dataset_text.py
# ===============================
from torch.utils.data import Dataset, DataLoader
import jieba
import numpy as np
def read_dict(voc_dict_path):
    voc_dict = {}
    dict_list = open(voc_dict_path, encoding='utf-8').readlines()
    for item in dict_list:
        item = item.split(",")
        voc_dict[item[0]] = int(item[1].strip())
    return voc_dict

def load_data(path, path_stop_words):

    data_list = data_path = open(path, encoding='utf-8').readlines()[1:]

    stop_words = open(path_stop_words, encoding='utf-8').readlines()[1:]
    stop_word_List = [line.strip() for line in stop_words]
    stop_word_List.append(" ")
    stop_word_List.append("\n")

    voc_dict = {}
    # min_seq = 1
    # top_n = 1000
    # UNK = "<UNK>"
    # PAD = "<PAD>"
    data = []
    max_len_seq = 0
    for item in data_list[:1000]:
        label = item[0]
        content = item[2:].strip()
        seg_list = jieba.cut(content, cut_all=False)
        seg_res = []
        for seg_item in seg_list:
            if seg_item in stop_word_List:
                continue
            seg_res.append(seg_item)
            if seg_item in voc_dict.keys():
                voc_dict[seg_item] = voc_dict[seg_item] + 1
            else:
                voc_dict[seg_item] = 1
        if len(seg_res) > max_len_seq:
            max_len_seq = len(seg_res)
        data.append([label, seg_res])
    return data, max_len_seq

class text_Cls(Dataset):
    def __init__(self, voc_dict_path, data_path, data_stop_path):
        self.data_path = "../data/weibo_text/weibo_senti_100k.csv"
        self.data_stop_path = "../data/weibo_text/hit_stopword"
        self.voc_dict = read_dict(voc_dict_path)
        self.data, self.max_seq_len = load_data(self.data_path, self.data_stop_path)

        np.random.shuffle(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        data = self.data[item]
        label = int(data[0])
        word_list = data[1]

        input_idx = []
        for word in word_list:
            if word in self.voc_dict.keys():
                input_idx.append(self.voc_dict[word])
            else:
                input_idx.append(self.voc_dict["<UNK>"])
        if len(input_idx) < self.max_seq_len:
            input_idx += [self.voc_dict["<PAD>"] for _ in range(self.max_seq_len - len(input_idx))]

        data = np.array(input_idx)

        return label, data


# def data_loader(data_path, data_stop_path, dict_path):
#     # data_path = "../data/weibo_text/weibo_senti_100k.csv"
#     # data_stop_path = "../data/weibo_text/hit_stopword"
#     # dict_path = "../data/weibo_text/dict"
#     dataset = text_Cls(dict_path, data_path, data_stop_path)
#     return DataLoader(dataset, batch_size=10, shuffle=True)

def data_loader(dataset, config):
    # data_path = "../data/weibo_text/weibo_senti_100k.csv"
    # data_stop_path = "../data/weibo_text/hit_stopword"
    # dict_path = "../data/weibo_text/dict"
    # dataset = text_Cls(dict_path, data_path, data_stop_path)
    return DataLoader(dataset, batch_size=config.batch_size, shuffle=config.is_shuffle)


if __name__ == '__main__':
    data_path = "../data/weibo_text/weibo_senti_100k.csv"
    data_stop_path = "../data/weibo_text/hit_stopword"
    dict_path = "../data/weibo_text/dict"
    train_data_loader = data_loader(data_path, data_stop_path, dict_path)
    for i, batch in enumerate(train_data_loader):
        print(batch)

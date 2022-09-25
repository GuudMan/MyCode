#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->run_test
# @Time      :2022/9/25 17:05
# @Author    :Peng neng
# @File      :run_test.py
# ===============================
import torch
import torch.nn as nn
from torch import optim
from model import Model
from dataset_text import data_loader, text_Cls
from config import Config

cfg = Config()

data_path = "../data/weibo_text/weibo_senti_100k.csv"
data_stop_path = "../data/weibo_text/hit_stopword"
dict_path = "../data/weibo_text/dict"
dataset = text_Cls(dict_path, data_path, data_stop_path)
train_dataloader = data_loader(dataset, cfg)
cfg.pad_size = dataset.max_seq_len

model_text_cls = Model(config=cfg)
model_text_cls.to(cfg.devices)
model_path = "../data/weibo_text/text_model/10.pth"
model_text_cls.load_state_dict(torch.load(model_path))

for i, batch in enumerate(train_dataloader):
    label, data = batch
    data = torch.tensor(data, dtype=torch.int64).to(cfg.devices)
    label = torch.tensor(label, dtype=torch.int64).to(cfg.devices)
    pred_softmax = model_text_cls.forward(data)
    print(pred_softmax)
    print(label)

    pred = torch.argmax(pred_softmax, dim=1)
    print(pred)

    out = torch.eq(pred, label)
    print(out)
    








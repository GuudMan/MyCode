#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->run_train
# @Time      :2022/9/25 16:29
# @Author    :Peng neng
# @File      :run_train.py
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

loss_func = nn.CrossEntropyLoss()

optimizer = optim.Adam(model_text_cls.parameters(), lr=cfg.learn_rate)

for epoch in range(cfg.num_epochs):
    for i, batch in enumerate(train_dataloader):
        label, data = batch
        data = torch.tensor(data, dtype=torch.int64).to(cfg.devices)
        label = torch.tensor(label, dtype=torch.int64).to(cfg.devices)

        optimizer.zero_grad()
        pred = model_text_cls.forward(data)

        loss_val = loss_func(pred, label)

        print("epoch is {}, ite is {}, val is {}".format(epoch, i, loss_val))
        loss_val.backward()

        optimizer.step()
    if epoch % 10 == 0:
        torch.save(model_text_cls.state_dict(), "../data/weibo_text/text_model/{}.pth".format(epoch))










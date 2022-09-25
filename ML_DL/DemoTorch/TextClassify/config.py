#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->config
# @Time      :2022/9/25 15:53
# @Author    :Peng neng
# @File      :config.py
# ===============================
import torch


class Config:
    def __init__(self):
        # self.embeding = nn.Embedding(config.n_vocab, config.embed_size, padding_idx=config.n_vocab - 1)
        # self.lstm = nn.LSTM(config.embed_size,
        #                     config.hidden_size,
        #                     config.num_layers,
        #                     bidirectional=True,
        #                     batch_first=True,
        #                     dropout=config.dropout)
        # self.maxpool = nn.MaxPool1d(config.pad_size)
        # self.fc = nn.Linear(config.hidden_size * 2 + config.embed_size,
        #                     config.num_class)
        # self.softmax = self.softmax(dim=1)
        self.n_vocab = 1002
        self.embed_size = 128
        self.hidden_size = 128
        self.num_layers = 3
        self.dropout = 0.8
        self.num_class = 2
        self.pad_size = 512
        self.batch_size = 128
        self.is_shuffle = True
        self.learn_rate = 0.001
        self.num_epochs = 100
        self.devices = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
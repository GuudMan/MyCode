#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->classify_regression
# @Time      :2022/8/12 20:45
# @Author    :Peng neng
# @File      :classify_regression.py
# 波士顿房价预测
# ===============================
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)
import torch
import re

df_data = pd.read_csv('../data/housing.data')
# 解析数据
ff = open('../data/housing.data').readlines()
data = []
for item in ff:
    # 将多个空格合并为一个空格
    out = re.sub(r"\s{2,}", " ", item).strip()
    data.append(out.split(" "))
data = np.array(data).astype(float)
print(data.shape)

y = data[:, -1]
x = data[:, 0:-1]
y_train = y[0:496]
y_test = y[496:]

x_train = x[0:496]
x_test = x[496:]

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# 搭建网络
# 回归网络
class Net(torch.nn.Module):
    def __init__(self, n_feature, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, 100)
        self.predict = torch.nn.Linear(100, n_output)

    def forward(self, x):
        out = self.hidden(x)
        out = torch.relu(out)
        out = self.predict(out)
        return out


net = Net(13, 1)
# 定义loss
loss_func = torch.nn.MSELoss()

# 定义优化器
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

# training
for i in range(10000):
    x_data = torch.tensor(x_train, dtype=torch.float32)
    y_data = torch.tensor(y_train, dtype=torch.float32)

    pred = net.forward(x_data)
    torch.squeeze(pred)
    loss = loss_func(pred, y_data) * 0.001

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print("ite:{}, loss:{}".format(i, loss))
    print(f"pred : {pred[:10]}")
    print(f"pred : {y_data[:10]}")

    # test
    x_data = torch.tensor(x_test, dtype=torch.float32)
    y_data = torch.tensor(y_test, dtype=torch.float32)

    pred = net.forward(x_data)
    torch.squeeze(pred)
    loss_test = loss_func(pred, y_data) * 0.001

    print("ite:{}, loss_test:{}".format(i, loss_test))

    # optimizer.zero_grad()
    # loss.backward()
    # optimizer.step()

torch.save(net, "../data/model.pkl")


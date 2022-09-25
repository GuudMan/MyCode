#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->train
# @Time      :2022/8/28 22:22
# @Author    :Peng neng
# @File      :train.py
# ===============================
import os

import networkx
import torch
import torch.nn as nn
import torchvision
import tensorboardX
from vggnet import VGGnet
from pre_resnet import pytorch_resnet18
from load_cifar10 import train_data_loader, test_data_loader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if __name__ == '__main__':
    epoch_num = 2
    lr = 0.01
    batch_size = 128
    net = pytorch_resnet18().to(device)

    # loss
    loss_func = nn.CrossEntropyLoss()
    # optimizer
    optimizer = torch.optim.Adam(net.parameters(), lr=lr)
    # optimizer = torch.optim.SGD(net.parameters(), lr=lr,
    #                             momentum=0.9,
    #                             weight_decay=5e-4)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.9)

    if not os.path.exists("log"):
        os.mkdir("log")

    writer = tensorboardX.SummaryWriter("log")
    step_n = 0
    for epoch in range(epoch_num):
        # print("epoch:", epoch)
        net.train()

        for i, data in enumerate(train_data_loader):
            # print("step:", i)
            # print("data", data)
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            # print("inputs.shape", inputs.shape )
            outputs = net(inputs)
            loss = loss_func(outputs, labels)

            # 设置初始梯度为0
            optimizer.zero_grad()

            # 反向传播
            loss.backward()

            # 更新梯度
            optimizer.step()

            # print("step: ", i, "loss is :", loss.item())

            # 计算准确率
            _, pred = torch.max(outputs.data, dim=1)

            correct = pred.eq(labels.data).cpu().sum()

            # print("train step", i, "loss is:", loss.item(),
            #       "mini-batch correct is:", 100.0 * correct / batch_size)

            writer.add_scalar("train loss", loss.item(), global_step=step_n)
            writer.add_scalar("train correct", correct.item() * 100 / batch_size
                              , global_step=step_n)

            im = torchvision.utils.make_grid(inputs)
            writer.add_image("train, im", im, global_step=step_n)
            step_n += 1

        if not os.path.exists("models"):
            os.mkdir("models")
        torch.save(net.state_dict(), "models/{}.pth".format(epoch + 1))
        scheduler.step()  # 更新学习率

        print("train lr is ", optimizer.state_dict()["param_groups"][0]["lr"])


        sum_loss = 0
        sum_correct = 0
        for i, data in enumerate(test_data_loader):
            net.eval()
            # print("step:", i)
            # print("data", data)
            inputs, labels = data
            inputs, labels = inputs.to(device), labels.to(device)
            # print("inputs.shape", inputs.shape )
            outputs = net(inputs)
            loss = loss_func(outputs, labels)

            # 计算准确率
            _, pred = torch.max(outputs.data, dim=1)

            correct = pred.eq(labels.data).cpu().sum()

            sum_loss = + loss.item()
            sum_correct += correct.item()
            # print("test step", i, "loss is:", loss.item(),
            #       "mini-batch correct is:", 100.0 * correct / batch_size)

            im = torchvision.utils.make_grid(inputs)
            writer.add_image("test, im", im, global_step=step_n)

            writer.add_scalar("test loss", loss.item(),  global_step=step_n)
            writer.add_scalar("test correct", correct.item() * 100 / batch_size, global_step=step_n)

        # if not os.path.exists("models"):
        #     os.mkdir("models")
        # torch.save(net.state_dict(), "models/{}.pth".format(epoch + 1))
        # scheduler.step()  # 更新学习率

        test_loss = sum_loss * 1.0 / len(test_data_loader)
        test_correct = sum_correct * 100.0 / len(test_data_loader) / batch_size
        print("test lr is ", "loss is:", test_loss, "test correct is:", test_correct)
        writer.close()














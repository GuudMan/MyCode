#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->手写数字识别
# @Time      :2022/8/13 14:20
# @Author    :Peng neng
# @File      :手写数字识别.py
# ===============================
import torch
import torchvision.datasets as dataset
import torchvision.transforms as transforms
import torch.utils.data as data_utils
import cv2

# data
train_data = dataset.MNIST(root="../data/mnist",
                           train=True,
                           transform=transforms.ToTensor(),
                           download=True)
test_data = dataset.MNIST(root="../data/mnist",
                           train=False,
                           transform=transforms.ToTensor(),
                           download=True)

# batchsize
train_loader = data_utils.DataLoader(dataset=train_data,
                                     batch_size=64,
                                     shuffle=True,
                                     )
test_loader = data_utils.DataLoader(dataset=test_data,
                                     batch_size=64,
                                     shuffle=True,
                                     )
# net
class CNN(torch.nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv = torch.nn.Sequential(
            torch.nn.Conv2d(1, 32, kernel_size=5, padding=2),
            torch.nn.BatchNorm2d(32),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2)
        )
        self.fc=torch.nn.Linear(14 * 14 * 32, 10)

    def forward(self, x):
        out = self.conv(x)
        out = out.view(out.size()[0], -1)
        out = self.fc(out)
        return out

cnn = CNN()

# loss
loss_func = torch.nn.CrossEntropyLoss()

# 优化
optimizer = torch.optim.Adam(cnn.parameters(), lr=0.01)

# 训练
for epoch in range(10):
    for i, (images, labels) in enumerate(train_loader):
        # images = images.cuda
        # labels = labels.cuda
        outputs = cnn(images)
        loss = loss_func(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print("epoch is {}, ite is {}/{}, "
              "loss is {}".format(epoch + 1, i,
                                  len(train_data) // 64,
                                  loss.item()))
# test
loss_test = 0
accuracy = 0
for i, (images, labels) in enumerate(test_loader):
    outputs = cnn(images)
    # batchsize = batchsize * cls_num
    loss_test += loss_func(outputs, labels)
    _, pred = outputs.max(1)
    accuracy += (pred == labels).sum().item()

    images = images.numpy()
    labels = labels.numpy()
    pred = pred.numpy()
    # batchsize * 1 * 28
    for idx in range(images.shape[0]):
        im_data = images[idx]
        im_label = labels[idx]
        im_pred = pred[idx]
        im_data = im_data.transpose(1, 2, 0)

        print("label", im_label)
        print("pred", im_pred)
        cv2.imshow("imdata", im_data)
        cv2.waitKey(0)


    accuracy = accuracy / len(test_data)
    print("accuracy is {}".format(accuracy))

# 保存

# 加载模型  inference
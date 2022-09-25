#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->load_cifar10
# @Time      :2022/8/17 15:42
# @Author    :Peng neng
# @File      :load_cifar10.py
# ===============================
import glob

from torchvision import transforms
from torch.utils.data import DataLoader, Dataset
import os
from PIL import Image
import numpy as np

label_name = ["airplane", "automobile",
              "bird", "cat", "deer", "dog",
              "frog", "horse", "ship", "truck"]
label_dict = {}

for idx, name in enumerate(label_name):
    label_dict[name] = idx

print(label_dict)


def default_loader(path):
    return Image.open(path).convert("RGB")


train_transform = transforms.Compose([
    transforms.RandomCrop(28),
    transforms.RandomHorizontalFlip(),
    # transforms.RandomVerticalFlip(),
    # transforms.RandomRotation(90),
    # transforms.RandomGrayscale(0.1),
    # transforms.ColorJitter(0.3, 0.3, 0.3, 0.3),
    transforms.ToTensor()
])

test_transform = transforms.Compose([
    transforms.RandomSizedCrop((28, 28)),
    # transforms.RandomHorizontalFlip(),
    # transforms.RandomVerticalFlip(),
    # transforms.RandomRotation(90),
    # transforms.RandomGrayscale(0.1),
    # transforms.ColorJitter(0.3, 0.3, 0.3, 0.3),
    transforms.ToTensor()
])


class MyDataSets(Dataset):
    def __init__(self, im_list, transform=None, loader=default_loader):
        super(MyDataSets, self).__init__()
        imgs = []
        for im_item in im_list:
            im_lable_name = im_item.split('\\')[-2]
            imgs.append([im_item, label_dict[im_lable_name]])

        self.imgs = imgs
        self.transform = transform
        self.loader = loader

    def __getitem__(self, index):
        im_path, im_label = self.imgs[index]

        im_data = self.loader(im_path)

        if self.transform is not None:
            im_data = self.transform(im_data)

        return im_data, im_label

    def __len__(self):
        return len(self.imgs)


im_train_list = glob.glob("../data/CIFAR10/TRAIN/*/*.png")
im_train_list = im_train_list[:5000]
im_test_list = glob.glob("../data/CIFAR10/TEST/*/*.png")
im_test_list = im_test_list[:1000]
train_dataset = MyDataSets(im_train_list, transform=train_transform)
test_dataset = MyDataSets(im_test_list, transform=test_transform)

train_data_loader = DataLoader(dataset=train_dataset,
                               batch_size=4,
                               shuffle=True,
                               num_workers=4)

test_data_loader = DataLoader(dataset=test_dataset,
                              batch_size=4,
                              shuffle=False,
                              num_workers=4)

print("num of train:", len(train_data_loader))
print("num of test:", len(test_data_loader))

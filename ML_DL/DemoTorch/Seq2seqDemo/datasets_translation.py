#! /usr/bin/env python
# -*- coding:utf-8 -*-
# ==============================
# @project ->File  :DemoTorch->datasets_translation
# @Time      :2022/9/25 21:41
# @Author    :Peng neng
# @File      :datasets_translation.py
# ===============================
import jieba
from utils import normalizeString,cht_to_chs

# 起始符
SOS_token = 0
# 终符
EOS_token = 1
MAX_LEN = 10

class Lang:
    def __init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2cont = {}
        self.index2word = {
            0: "SOS", 1: "EOS"
        }
        self.n_words = 2

    def addSentence(self, sentence):
        for word in sentence.split(" "):
            self.addWord(word)


    def addWord(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.n_words
            self.word2cont = 1
            self.index2word[self.n_words] = word
            self.n_words += 1
        else:
            self.word2index[word] += 1


def readLangs(lang1, lang2, path):
    lines = open(path, encoding='utf-8').readlines()

    lang1_cls = Lang(lang1)
    lang2_cls = Lang(lang2)


    pairs = []
    for l in lines:
        l = l.split("\t")
        sentence1 = normalizeString(l[0])
        sentence2 = cht_to_chs(l[1])
        seq_list = jieba.cut(sentence2, cut_all=False)
        sentence2 = " ".join(seq_list)

        if len(sentence1.split(" ")) > MAX_LEN:
            continue
        if len(sentence2.split(" ")) > MAX_LEN:
            continue

        pairs.append([sentence1, sentence2])
        lang1_cls.addSentence(sentence1)
        lang2_cls.addSentence(sentence2)

    return lang1_cls, lang2_cls, pairs


lang1 = "en"
lang2 = "cn"
path = '../data/translation/en-cn.txt'
lang1_cls, lang2_cls, pairs = readLangs(lang1, lang2, path)
print(len(pairs))
print(lang1_cls.n_words)
print(lang2_cls.n_words)
print(lang1_cls.index2word)
print(lang2_cls.index2word)

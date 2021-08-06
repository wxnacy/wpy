#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
工具
"""

from functools import cmp_to_key
from collections import defaultdict

def search(datas, word):
    """
    搜索
    :param list datas: 单词列表
    :param str word: 搜索的单词
    :results list 搜索结果，按照匹配位置排序
    """
    patten = defaultdict(int)
    for o in datas:
        patten[o] = -1
        p = o.lower()
        if word not in p:
            continue
        patten[o] = p.index(word)
    res = list(filter(lambda x: patten[x] > -1, datas))
    res.sort(key = lambda x: patten[x])
    return res

def sortd_plus(arr, sorter=None, reverse=False):
    """
    排序
    :param list arr: 数组
    :param list sorter: 排序方式
        [('age', 1), ('id', -1)]    age 按照正序，相同时 id 倒序
    :param bool reverse: 是否倒序
    """
    def _sort(a, b):
        for name, sort_by in sorter:
            if a[name] < b[name]:
                return -sort_by
            elif a[name] > b[name]:
                return sort_by

        return 0

    if sorter:
        arr.sort(key=cmp_to_key(_sort))
    else:
        arr.sort(reverse = reverse)

    return arr

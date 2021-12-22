#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
字符串相关测试
"""
from collections import defaultdict

#  __all__ = [
    #  "search",
#  ]

#  def search(datas, word):
    #  """
    #  搜索
    #  :param list datas: 单词列表
    #  :param str word: 搜索的单词
    #  :results list 搜索结果，按照匹配位置排序
    #  """
    #  patten = defaultdict(int)
    #  for o in datas:
        #  patten[o] = -1
        #  p = o.lower()
        #  if word not in p:
            #  continue
        #  patten[o] = p.index(word)
    #  res = list(filter(lambda x: patten[x] > -1, datas))
    #  res.sort(key = lambda x: patten[x])
    #  return res

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
list 工具模块
"""

from functools import cmp_to_key

class ListUtils(object):

    @classmethod
    def sorted_plus(cls, arr, sorter=None, reverse=False):
        """
        排序
        :param list arr: 数组
        :param list sorter: 排序方式
            [('age', 1), ('id', -1)]    age 按照正序，相同时 id 倒序
        :param bool reverse: 是否倒序
        """
        def _sort(a, b):
            for name, sort_by in sorter:
                a_val = a.get(name)
                b_val = b.get(name)
                if a_val is None:
                    return -sort_by
                if b_val is None:
                    return sort_by
                if a_val < b_val:
                    return -sort_by
                elif a_val > b_val:
                    return sort_by

            return 0

        if sorter:
            arr.sort(key=cmp_to_key(_sort))
        else:
            arr.sort(reverse = reverse)

        return arr

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
随机方法
"""

import pytest

from wpy.tools import tools

def test_sortd_plus():
    """排序增强"""
    arr = [3, 5, 2, 4, 1]
    tools.sortd_plus(arr)
    assert arr == [1, 2, 3, 4, 5]

    arr = [{"age": 5, "id": 2}, {"age": 5, "id": 5}, {"age": 3, "id": 4}]
    tools.sortd_plus(arr, [('age', 1), ('id', -1)])
    assert arr == [{"age": 3, "id": 4},{"age": 5, "id": 5}, {"age": 5, "id": 2}]

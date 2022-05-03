#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
格式化模块
"""


from wpy import format_size

def test_format_size():
    """格式化 size"""

    assert '102B' == format_size(102)
    assert '1K' == format_size(1024)
    assert '1.98K' == format_size(2024)
    assert '1.86M' == format_size(1024 **2 + 900000)
    assert '1.84G' == format_size(1024 **3 + 900000000)
    assert '1.39T' == format_size(1024 **4 + 1024 ** 3 * 400)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
随机方法
"""

import pytest

from wpy.tools.format import Format

def test_format_size():
    """格式化 size"""

    assert '102B' == Format.format_size(102)
    assert '1K' == Format.format_size(1024)
    assert '1.98K' == Format.format_size(2024)
    assert '1.86M' == Format.format_size(1024 **2 + 900000)
    assert '1.84G' == Format.format_size(1024 **3 + 900000000)
    assert '1.39T' == Format.format_size(1024 **4 + 1024 ** 3 * 400)

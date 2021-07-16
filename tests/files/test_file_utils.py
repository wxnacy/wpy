#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
随机方法
"""

import pytest

from wpy.files import FileUtils
from wpy.tools import randoms

def test_read_write():
    """读写"""

    data = {"name": "wxnacy"}
    path = '/tmp/wpy_{}.yml'.format(randoms.random_int(6))
    FileUtils.write_yml(path, data)

    res = FileUtils.read_dict(path)
    assert data, res

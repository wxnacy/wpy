#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
"""
path 模块测试用例
"""

import random
from wpy import path

test_data_dir = 'tests/data'

def test_walkfile():
    paths = path.walkfile(test_data_dir)
    paths = [o for o in paths]
    assert len(paths) == 4

    paths = path.walkfile(test_data_dir, suffixs=['json'])
    paths = [o for o in paths]
    assert len(paths) == 1

def test_getsize():
    assert path.getsize('tests/data/a.txt') == 7
    assert path.getsize('tests/data/c') == 26

def test_write_yml():
    """读写"""

    data = {"name": "wxnacy"}
    _path = f'/tmp/wpy_{random.randint(9000, 10000)}.yml'
    path.write_yml(_path, data)

    res = path.read_dict(_path)
    assert data, res

def test_zip():
    path.zip(test_data_dir, '/tmp')
    assert path.getsize('/tmp/data.zip') == 456

    path.zip('tests/data/', '/tmp')
    assert path.getsize('/tmp/data.zip') == 456

    path.zip(test_data_dir, '/tmp/data2.zip')
    assert path.getsize('/tmp/data2.zip') == 456

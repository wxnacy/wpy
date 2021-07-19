#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
文件工具类
"""

import os
import json
import yaml

class FileUtils:

    @classmethod
    def read_dict(cls, filepath):
        """
        读取字典数据
        :param str filepath: 文件地址
        """
        with open(filepath, 'r') as f:
            if filepath.endswith('.yml'):
                return yaml.safe_load(f)
            lines = f.readlines()
        return json.loads(''.join(lines))

    @classmethod
    def write_yml(cls, filepath, data):
        """保存成 yml 格式文件"""
        filepath = os.path.expanduser(filepath)
        with open(filepath, 'w') as f:
            yaml.dump(data, f)

    @classmethod
    def write_dict(cls, filepath, data):
        """保存成 dict 格式文件"""
        filepath = os.path.expanduser(filepath)
        with open(filepath, 'w') as f:
            f.write(json.dumps(data, indent=4))

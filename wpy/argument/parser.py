#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""

"""
from argparse import Namespace
from collections import deque

from .enum import Action

class ArgumentNamespace(Namespace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def has_args(self):
        """是否包含参数"""
        count = 0
        for k, v in self.__dict__.items():
            if v:
                count += 1
        return count > 1

class Argument(object):
    name = ''
    short_name = ''
    is_cmd = False
    action = ''
    value = None
    required = False

    def __init__(self, name, action):
        self.name = name.replace('--', '')
        self.is_cmd = True if not name.startswith('--') else False
        self.required = True if self.is_cmd else False
        self.action = action
        self.clear()

    def clear(self):
        self.value = None
        if self.action == Action.STORE_TRUE.value:
            self.value = False
        if self.action == Action.APPEND.value:
            self.value = []

    @property
    def is_list(self):
        return isinstance(self.value, list)

class ArgumentParser(object):
    cmd = ''
    cmd_arg = None
    _arg_dict = None
    argument = None

    def __init__(self, ):
        self._arg_dict = {}
        self.add_argument('--verbose', action=Action.STORE_TRUE.value)

    def add_argument(self, *args, action=None):
        """
        添加参数
        """
        if not action:
            action = Action.STORE.value
        arg = Argument(args[0], action)
        if arg.is_cmd:
            self.cmd_arg = arg
        self._arg_dict[arg.name] = arg

    def get_arguments(self):
        """
        获取参数列表
        """
        return self._arg_dict.values()

    @property
    def _argument_namespace(self):
        return ArgumentNamespace

    def parse_args(self, args):
        if not args:
            return None
        args = args if isinstance(args, list) else args.split(" ")
        self._parse_args(args)
        res = self._make_args_dict(args)
        argument = self._make_argument_namespace(**res)
        self.argument = argument
        return argument

    def _make_args_dict(self, args):
        """创建参数键值对"""
        res = {}
        for arg in self.get_arguments():
            res[arg.name] = arg.value
        res[self.cmd_arg.name] = self.cmd_arg.value
        return res

    def _make_argument_namespace(self, **res):
        return self._argument_namespace(**res)

    def _parse_args(self, args):
        args_len = len(args)
        if args_len == 0:
            return None
        # 清空数据
        for _, arg in self._arg_dict.items():
            arg.clear()
        # 赋值命令参数
        self.cmd_arg.value = args[0]
        i = 1
        while i < args_len:
            item = args[i]
            if not item.startswith('--'):
                i += 1
                continue
            key = item.replace('--', '')
            arg = self._arg_dict.get(key)
            if not arg:
                i += 1
                continue
            if arg.action == Action.STORE_TRUE.value:
                arg.value = True
            else:
                val_index = i + 1
                if val_index < args_len:
                    if arg.action == Action.APPEND.value:
                        arg.value.append(args[val_index])
                    else:
                        arg.value = args[val_index]
                    i += 1
            i += 1


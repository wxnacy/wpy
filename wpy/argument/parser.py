#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""

"""
from argparse import Namespace
#  from collections import deque

from wpy.base import BaseObject
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

class Argument(BaseObject):
    name = ''           # 参数名称 --name
    help = ''           # 参数帮忙文档
    short_name = ''     # 短名称 -n
    action = ''         # 参数种类
    is_cmd = False      # 是否为命令参数
    value = None        # 值
    required = False    # 是否为必须
    datatype = None     # 数据类型
    default = None      # 默认值
    _is_set = False

    def __init__(self, name, action, **kwargs):
        kwargs['name'] = name
        kwargs['action'] = action
        super().__init__(**kwargs)
        self.clear()

    @property
    def is_set(self):
        return self._is_set

    def set_value(self, value):
        self.value = self._format_value(value)
        self._is_set = True

    def _format_value(self, value):
        if value == None and self.datatype:
            return self.datatype()
        if value == None:
            return value
        return self.datatype(value) if self.datatype and not isinstance(
                value, self.datatype) else value

    def add_value(self, value):
        if self.action == Action.APPEND.value:
            self.value.append(self._format_value(value))
            self._is_set = True
        else:
            self.set_value(value)

    def clear(self):
        self._is_set = False
        self.value = None
        if self.action == Action.STORE_TRUE.value:
            self.value = self.default or False
        elif self.action == Action.APPEND.value:
            self.value = self.default or []
        else:
            self.value = self.default
            if self.datatype and self.value:
                self.value = self.datatype(self.value)

    @property
    def is_list(self):
        return isinstance(self.value, list)

class ArgumentParser(object):
    cmd_arg = None
    _arg_dict = None
    _short_arg_dict = None
    argument = None

    def __init__(self, ):
        self._arg_dict = {}
        self._short_arg_dict = {}
        self.add_argument('--verbose', action=Action.STORE_TRUE.value)

    def add_argument(self, *args, action=Action.STORE.value, **kwargs):
        """
        添加参数
        """
        name = None
        is_cmd = False
        short_name = None
        for _arg in args:
            if _arg.startswith('--'):
                name = self._conver_arg_name(_arg) or name
            elif _arg.startswith('-'):
                short_name = self._conver_arg_short_name(_arg) or short_name
            else:
                # 命令类型参数只能设置一个
                if len(args) > 1:
                    raise ValueError('command vargument only can set one')
                name = self._conver_arg_name(_arg) or name
                is_cmd = True

        # 至少设置一个参数名称
        if not name and not short_name:
            raise ValueError('add_argument must set args')

        kwargs['short_name'] = short_name
        kwargs['is_cmd'] = is_cmd
        arg = Argument(name, action, **kwargs)
        if is_cmd:
            self.cmd_arg = arg
        self._arg_dict[arg.name] = arg
        if short_name:
            self._short_arg_dict[short_name] = arg

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
            if arg.name:
                res[arg.name.replace('-', '_')] = arg.value
            if arg.short_name:
                res[arg.short_name.replace('-', '_')] = arg.value
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
            name = None
            short_name = None
            if item.startswith('--'):
                name = self._conver_arg_name(item)
            elif item.startswith('-'):
                short_name = self._conver_arg_short_name(item)
            if not name and not short_name:
                i += 1
                continue
            arg = self._arg_dict.get(name) or self._short_arg_dict.get(
                short_name)
            if not arg:
                i += 1
                continue
            if arg.action == Action.STORE_TRUE.value:
                arg.set_value(True)
            else:
                val_index = i + 1
                if val_index < args_len:
                    # 列表增加数据
                    arg.add_value(args[val_index])
                    i += 1
            i += 1

    @classmethod
    def _conver_arg_name(cls, text):
        """转参数名"""
        if text:
            if text.startswith('--'):
                text = text[2:]
                if not text:
                    raise ValueError('-- is not argument name')

                return text
            if text.startswith('-'):
                return None
            return text
        return None

    @classmethod
    def _conver_arg_short_name(cls, text):
        """转参数短名"""
        if text and text.startswith('-') and not text.startswith('--'):
            text = text[1:]
            if not text:
                raise ValueError('- is not argument name')
            return text
        return None

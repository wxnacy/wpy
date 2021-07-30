#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""

"""
import abc
from .parser import ArgumentParser

class CommandArgumentParser(ArgumentParser, metaclass=abc.ABCMeta):
    cmd = ''
    _prompt = None

    def set_prompt(self, prompt):
        self._prompt = prompt

    @abc.abstractmethod
    def default(cls):
        """
        初始化一个默认实例
        """
        pass

    @abc.abstractmethod
    def run(self, args):
        """运行"""
        pass

    def _print(self, line):
        """打印文本"""
        print(line)


class DefaultCommandArgumentParser(CommandArgumentParser):

    @classmethod
    def default(cls):
        item = cls()
        item.add_argument('cmd')
        return item

    def run(self, args):
        pass

class CommandArgumentParserFactory():
    _argparser = {}

    @classmethod
    def build_parser(cls, text=None):
        """根据命令构建参数解析器"""
        cmd = None
        if text:
            args = DefaultCommandArgumentParser.default().parse_args(text)
            cmd = args.cmd
        Parser = cls._argparser.get(cmd, DefaultCommandArgumentParser)
        return Parser.default()

    @classmethod
    def get_cmd_names(cls):
        return cls._argparser.keys()

    @classmethod
    def register(cls, active=True):
        def decorate(func):
            #  logger.info('register active=%s func %s.%s', active, func.__module__,
                #  func)
            #  if isinstance(func, str):
                #  raise Exception('can not register str')
            if not issubclass(func, CommandArgumentParser):
                raise Exception('only one register CommandArgumentParser subclass')
            if active:
                cls._argparser[func.cmd] = func
            else:
                cls._argparser.pop(func.cmd, None)

            return func
        return decorate


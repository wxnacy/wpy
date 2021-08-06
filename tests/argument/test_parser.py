#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""

"""

from wpy.argument import ArgumentParser
from wpy.argument import Argument
from wpy.argument import Action

def test_parse_args():
    parser = ArgumentParser()
    parser.add_argument('cmd')
    parser.add_argument('--config', help='配置地址')
    parser.add_argument('--module')
    parser.add_argument('--name')
    parser.add_argument('--save', action=Action.STORE_TRUE.value)
    parser.add_argument('--params', action=Action.APPEND.value)

    arguments = parser.get_arguments()
    for arg in arguments:
        if arg.name == 'config':
            assert arg.help == '配置地址'

    line = 'run'
    arg = parser.parse_args(line)
    assert arg.cmd == 'run'
    assert arg.save is False

    line = 'env --save'
    arg = parser.parse_args(line)
    assert arg.cmd == 'env'
    assert arg.save == True

    line = 'run --config config'
    arg = parser.parse_args(line)
    assert arg.cmd == 'run'
    assert arg.config == 'config'

    line = 'run --config config --module default'
    arg = parser.parse_args(line)
    assert arg.cmd == 'run'
    assert arg.config == 'config'
    assert arg.module == 'default'

    line = 'run --config config --name test name'
    arg = parser.parse_args(line)
    assert arg.cmd == 'run'
    assert arg.config == 'config'
    #  assert arg.name == 'test name'

    line = 'run --name test name --config config'
    arg = parser.parse_args(line)
    assert arg.cmd == 'run'
    assert arg.config == 'config'
    #  assert arg.name == 'test name'

    line = 'run --params key=value --params name=wxnacy --config config'
    arg = parser.parse_args(line)
    assert arg.cmd == 'run'
    assert arg.config == 'config'
    assert arg.params == ['key=value', 'name=wxnacy']

def test_parse_args_default():
    parser = ArgumentParser()
    parser.add_argument('cmd')
    parser.add_argument('--page', datatype=int, default=1)
    parser.add_argument('--name')

    args = parser.parse_args('run ')
    assert args.page == 1
    assert isinstance(args.page, int)

    args = parser.parse_args('run --page 3')
    assert args.page == 3
    assert isinstance(args.page, int)

    args = parser.parse_args('run --name 3')
    assert args.name == '3'
    assert isinstance(args.name, str)

def test_argument():
    arg = Argument('--page', Action.STORE.value, datatype=int, default=1)
    assert arg.name == 'page'
    assert arg.value == 1
    assert isinstance(arg.value, int)

    arg.set_value('3')
    assert arg.value == 3

    arg = Argument('--name', Action.STORE.value,)
    assert arg.value == None
    arg.set_value(3)
    assert arg.value == 3
    assert isinstance(arg.value, int)

    arg = Argument('--name', Action.STORE.value, datatype = str)
    assert arg.value == None
    arg.set_value(3)
    assert arg.value == '3'
    assert isinstance(arg.value, str)

    arg = Argument('--open', Action.STORE_TRUE.value)
    assert arg.value == False

    arg = Argument('--open', Action.STORE_TRUE.value, default=True)
    assert arg.value == True

    arg = Argument('--open', Action.APPEND.value)
    assert arg.value == []

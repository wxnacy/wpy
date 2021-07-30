#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""

"""

from wpy.argument import CommandArgumentParserFactory
from wpy.argument import HistoryArgumentParser
from wpy.argument import CommandArgumentParser
from wpy.argument import DefaultCommandArgumentParser

def test_factory():
    parser = CommandArgumentParserFactory.build_parser()
    assert isinstance(parser, DefaultCommandArgumentParser)

    parser = CommandArgumentParserFactory.build_parser('history')
    assert isinstance(parser, HistoryArgumentParser)

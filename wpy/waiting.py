#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import asyncio
from functools import wraps
import itertools
import sys
import time

@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = f'{char}  {msg}'
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))

def waiting(msg='thinking!'):
    def wraped(func):
        @wraps(func)
        def _wrap(*args, **kw):
            def _supervisor():
                spinner = asyncio.async(spin(msg))
                result = yield from func(*args, **kw)
                spinner.cancel()
                return result
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(_supervisor())
            loop.close()
            return result
        return _wrap
    return wraped

@waiting()
@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(1)
    #  print('success')
    return 42

if __name__ == "__main__":
    #  main()
    slow_function()
    print('success')

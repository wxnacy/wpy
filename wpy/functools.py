#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:  常用的装饰器

import timeit

CLOCK_FMT = '[{T:0.8f}s] {F}({A}, {K}) -> {R}'
def clock(times=1, fmt=CLOCK_FMT, logger_func=print):
    def clock_wraper(func):
        def _wraper(*args, **kwargs):
            t0 = timeit.default_timer()
            result = None
            for i in range(times):
                result = func(*args, **kwargs)
            T = timeit.default_timer() - t0
            F = func.__name__
            A = args
            K = kwargs
            print(repr(args))
            R = repr(result)
            logger_func(fmt.format(**locals()))
            return result
        return _wraper
    return clock_wraper


if __name__ == "__main__":
    @clock()
    def test(*args, **kw):
        r = 0
        for i in range(10000):
            r += i

    test(1, 'a')




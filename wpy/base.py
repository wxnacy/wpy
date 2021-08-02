#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import json
from enum import Enum

class BaseObject(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return json.loads(self.to_json())

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    def format(self):
        return self.to_dict()

    def __str__(self):
        return self.to_json()


class BaseEnum(Enum):
    """枚举基类"""

    @classmethod
    def values(cls):
        return [x.value for _, x in cls.__members__.items()]

    @classmethod
    def is_valid(cls, value):
        return value in cls.values()

    @classmethod
    def get_by_value(cls, state_value):
        for name, member in cls._member_map_.items():
            if state_value == member.value:
                return member

        return None

    @classmethod
    def validate(cls, value):
        """验证枚举值"""
        if value not in cls.values():
            raise ValueError('不支持的枚举值: {val}'.format(val=value))

    def __str__(self):
        return self.value

class BaseFactory(object):
    _factory = {}
    object_cls = object
    default_cls = None
    key = 'name'
    instance_func = None

    @classmethod
    def build(cls, name=None):
        """构建"""
        clazz = cls._factory.get(name) or cls.default_cls
        return clazz

    @classmethod
    def build_instance(cls, name=None):
        """构建实例"""
        clazz = cls.build(name)
        if not clazz:
            return None
        if cls.instance_func:
            return getattr(clazz, cls.instance_func)()
        return clazz()

    @classmethod
    def get_factory_keys(cls):
        return cls._factory.keys()

    @classmethod
    def register(cls, active=True):
        def decorate(func):
            if not issubclass(func, cls.object_cls):
                raise Exception('only one register {} subclass'.format(
                    cls.object_cls))
            key = getattr(func, cls.key)
            if active:
                cls._factory[key] = func
            else:
                cls._factory.pop(key, None)
            return func
        return decorate

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

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import pytest
from wpy import BaseObject, BaseEnum, BaseFactory

class User(BaseObject):
    id = 0
    name = None


def test_base_object():
    user = User(id=1, name='wxnacy')
    assert user.id == 1
    assert user.name == "wxnacy"
    assert user.dict() == { "id": 1, "name": "wxnacy" }


class StatusEnum(BaseEnum):
    SUCCESS = 'success'
    FAILED = 'failed'

def test_base_enum():

    assert StatusEnum.values() == ['success', 'failed']

    assert StatusEnum.is_valid(StatusEnum.SUCCESS.value)

    assert not StatusEnum.is_valid('test')

    assert StatusEnum.get_by_value(StatusEnum.SUCCESS.value
        ) == StatusEnum.SUCCESS

    with pytest.raises(ValueError) as e:
        StatusEnum.validate('test')
        assert str(e) == '不支持的枚举值: test'

    assert str(StatusEnum.FAILED) == StatusEnum.FAILED.value

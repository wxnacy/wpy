#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy@gmail.com
"""
随机方法
"""

import pytest
import os

from wpy.db import FileStorage
from wpy.db import FileStorageError
from wpy.files import FileUtils
from wpy.tools import randoms

root = '/tmp'
#  root = '~/Downloads'
db_name = 'wpy_db'
table = 'wpy_table'
table_root = os.path.join(os.path.expanduser(root), db_name, table)
db = FileStorage(root).get_db(db_name).get_table(table)

def _origin_data(data):
    for k in ('_id', '_update_time', "_create_time"):
        data.pop(k, None)
    return data

def test_insert():
    name = randoms.random_str(6)
    doc = {
        "name": name
    }
    _id = db.insert(doc)

    path = os.path.join(table_root, _id)
    data = FileUtils.read_dict(path)
    data = _origin_data(data)
    assert doc == data

    data = db.find_one_by_id(_id)
    data = _origin_data(data)
    assert doc == data

    doc['_id'] = _id
    with pytest.raises(FileStorageError) as excinfo:
        db.insert(doc)
        assert str(excinfo) == '{}._id {} is exists'.format(table, _id)

    db.drop()

    assert not os.path.exists(table_root)

def test_find():
    name = randoms.random_str(6)
    doc = { "name": name}
    db.insert(doc)
    db.insert(doc)
    doc['age'] = 12
    db.insert(doc)

    docs = db.find({ "name": name })
    assert len(docs) == 3

    docs = db.find({ "name": name, "age": 12 })
    assert len(docs) == 1

    db.drop()

def test_update():
    name = randoms.random_str(6)
    doc = { "name": name}
    db.insert(doc)
    _id = db.insert(doc)
    db.insert(doc)

    count = db.update(doc, {"name": "wxnacy"})
    assert count == 3

    data = db.find_one_by_id(_id)
    data = _origin_data(data)
    #  assert { "name": "wxnacy" } == data

    db.drop()

def test_delete():
    name = randoms.random_str(6)
    doc = { "name": name}
    db.insert(doc)
    _id = db.insert(doc)
    db.insert(doc)

    count = db.delete(doc)
    assert count == 3

    db.drop()

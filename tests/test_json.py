#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:

import unittest
from wpy import JSON


class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def teardown(self):
        pass

    def test_filter(self):
        book = dict(id = 2, name = 'size', price = 5)
        user = dict(id = 1, name = "wxnacy", book= book)

        res = JSON.filter(source = user, source_include=['id', 'book'])
        data = dict(id = 1, book= book)
        self.assertEqual(res, data)

        res = JSON.filter(user, 'id', 'book')
        data = dict(id = 1, book= book)
        self.assertEqual(res, data)
        res = JSON.filter(user, 'id', 'book.id')
        data = dict(id = 1, book= dict(id = 2))
        self.assertEqual(res, data)
        res = JSON.filter(user, 'id', 'book[id,name]')
        data = dict(id = 1, book= dict(id = 2, name = "size"))
        self.assertEqual(res, data)
        res = JSON.filter(user, source_exclude=['name', 'book'])
        data = dict(id = 1)
        self.assertEqual(res, data)
        res = JSON.filter(user, source_exclude=['name', 'book.price'])
        data = dict(id = 1, book= dict(id = 2, name = "size"))
        self.assertEqual(res, data)
        res = JSON.filter(user, source_exclude=['name', 'book[id,price]'])
        data = dict(id = 1, book= dict(name = "size"))
        self.assertEqual(res, data)

    def test_getattr(self):

        book = dict(id = 2, name = 'size', price = 5)
        user = dict(id = 1, name = "wxnacy", book= book)
        user = JSON.BaseDict(user)
        self.assertEqual(1, user.id)
        self.assertEqual(book, user.book)


if __name__ == "__main__":
    unittest.main()

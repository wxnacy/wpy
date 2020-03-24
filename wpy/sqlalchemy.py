#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: wxnacy(wxnacy@gmail.com)
# Description:


class SQLAlchemy():
    def __init__(self, *args, **kwargs):
        if args:
            self.database_uri = args[0]



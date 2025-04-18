#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : __init__.py

from app.aea import AEA


class MAC(AEA):
    def __init__(self):
        super().__init__()
        self.journal = "mac"
        self.base_url = f"https://www.aeaweb.org/journals/{self.journal}/"

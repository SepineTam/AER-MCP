#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : __init__.py

from app.aea import AEA


class AER(AEA):
    def __init__(self):
        super().__init__()
        self.journal = "aer"
        self.base_url = f"https://www.aeaweb.org/journals/{self.journal}/"


if __name__ == "__main__":
    aer = AER()
    print(aer.article_path_url("10.1257/aer.115.4.1059"))

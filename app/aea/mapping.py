#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : mapping.py

from app.aea import aer, aeri, app, pol, mac, mic

def mapping(class_name: str):
    mapping_dict = {
        "aer": aer.AER,
        "aeri": aeri.AERI,
        "app": app.APP,
        "pol": pol.POL,
        "mac": mac.MAC,
        "mic": mic.MIC
    }

    return mapping_dict.get(class_name)

#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : fake_ua.py

import random
from fake_useragent import UserAgent
import time


def get_random_headers():
    ua = UserAgent()
    user_agent = ua.random

    ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

    referers = [
        'https://www.google.com/',
        'https://www.bing.com/',
        'https://www.aeaweb.org/',
        'https://scholar.google.com/',
        'https://www.statamcp.com/'
    ]

    headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        # 'Accept-Language': random.choice(languages),
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'X-Forwarded-For': ip,
        'X-Real-IP': ip,
        'Client-IP': ip,
        'Referer': random.choice(referers),
        'Cache-Control': 'max-age=0',
        'Pragma': 'no-cache'
    }
    return headers


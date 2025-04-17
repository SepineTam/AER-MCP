#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : doi.py

import requests
from typing import Any


def get_doi_metadata(doi: str) -> Any | None:
    """
    Get metadata of academic paper via doi of paper

    Args:
        doi (str): The doi of paper, e.g. '10.1257/aer.20181249'

    Returns:
        dict: metadata dictionary
    """
    # API URL
    base_url = "https://api.crossref.org/works/"
    url = base_url + doi

    # request header, the official recommend add your email (not necessary)
    mail_address = "your-email@example.com"
    headers = {
        'User-Agent': f'Python-Script/1.0 (mailto:{mail_address})'
    }

    try:
        # get requests
        response = requests.get(url, headers=headers)

        # check whether success
        if response.status_code == 200:
            data = response.json()
            return data['message']
        else:
            print(f"WRONG, STATUS_CODE: {response.status_code}")
            return None
    except Exception as e:
        print(f"WRONG: {str(e)}")
        return None


# 使用示例
if __name__ == "__main__":
    sample_doi = "10.1257/aer.20181249"
    result = get_doi_metadata(sample_doi)
    print(result.keys())

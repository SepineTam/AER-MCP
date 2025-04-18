#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2025 - Present Sepine Tam, Inc. All Rights Reserved
#
# @Author : Sepine Tam
# @Email  : sepinetam@gmail.com
# @File   : __init__.py

import requests
from bs4 import BeautifulSoup

from app.utils import fake_ua

class AEA:
    def __init__(self):
        self.home_url = "https://www.aeaweb.org/"
        self.base_url = None

    def article_path_url(self, doi):
        url = self.home_url + f"articles?id={doi}"
        return url

    @staticmethod
    def _extract_id(response: requests.models.Response) -> list:
        if response.status_code != 200:
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        container = soup.find(class_="journal-article-group")

        if not container:
            return []

        articles = container.find_all('article', class_="journal-article")
        article_ids = [article.get('id') for article in articles if article.has_attr('id')]
        return article_ids

    def search(self,
               q: str,
               search_in_title: bool = True,
               search_in_abstract: bool = True,
               search_in_author: bool = True,
               jel_class: str = None,
               journal: bool = True
               ) -> list:
        if self.base_url:
            base_url = self.base_url + "search-results?"
        else:
            base_url = "https://www.aeaweb.org/journals/aer/search-results?"

        params = []
        if search_in_title:
            params.append("ArticleSearch[within][articletitle]=1")
        if search_in_abstract:
            params.append("ArticleSearch[within][articleabstract]=1")
        if search_in_author:
            params.append("ArticleSearch[within][authorlast]=1")
        if jel_class is not None:
            params.append(f"JelClass[value]={jel_class}")
        if journal:
            params.append("journal=1")

        params.append(f"ArticleSearch[q]={q}")
        search_url = base_url + "&".join(params)

        fake_headers = fake_ua.get_random_headers()
        resp = requests.get(search_url, headers=fake_headers)

        return self._extract_id(resp)


if __name__ == "__main__":
    sample_doi = "10.1257/aer.115.4.1059"
    aea = AEA()
    print(aea.search("skill"))

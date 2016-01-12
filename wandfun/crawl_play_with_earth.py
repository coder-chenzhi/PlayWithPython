# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'chenzhi'

import requests
from bs4 import BeautifulSoup

HOMEPAGE_URL = "https://wap.koudaitong.com/v2/showcase/feature?alias=1g88ybn4d"

HOMEPAGE_URL2 = "https://wap.koudaitong.com/v2/showcase/feature?alias=jjpp84aa"

# get all articles' url from homepage
def get_all_articles(url):

    r = requests.get(url)
    page = r.content
    soup = BeautifulSoup(page)
    main_content_div = soup.find("div", class_="custom-richtext js-lazy-container js-view-image-list")
    all_herf = main_content_div.find_all("a")
    all_url = [href["href"] for href in all_herf]
    # print "\n".join(all_url)
    return all_url


def get_info(url):
    r = requests.get(url)
    page = r.content
    soup = BeautifulSoup(page)
    title = soup.find("h2", id="activity-name").text.strip()
    print title

    time = soup.find("em", id="post-date").text
    author = soup.find_all("em", class_="rich_media_meta rich_media_meta_text")[1].text
    account = soup.find("a", id="post-user").text
    print time, author, account

if __name__ == "__main__":
    urls = get_all_articles(HOMEPAGE_URL2)
    for url in urls:
        print url
        get_info(url)
        print ""




# -*- coding: utf-8 -*-
__author__ = 'chenzhi'

from douban_client import DoubanClient
import json
import requests

if __name__ == "__main__":

    API_KEY = '0f2474e49ff2674d2d6d5eaddfd735e7'
    API_SECRET = 'ffc1f3ef21a0f872'

    # 在 OAuth 2.0 中，
    # 获取权限需要指定相应的 scope，请注意!!
    # scope 权限可以在申请应用的 "API 权限" 查看。

    # set token
    USER = "douban_basic_common, community_basic_user"
    BOOK_SCOPE = "book_basic_r, book_basic_w, douban_basic_common"
    MOVIE_BASIC_SCOPE = "movie_basic_r, movie_basic_w"
    MOVIE_ADVANCED_SCOPE = "movie_advance_r, movie_advance_w"
    SCOPE = " ,".join([USER, BOOK_SCOPE, MOVIE_ADVANCED_SCOPE, MOVIE_BASIC_SCOPE])
    print SCOPE

    your_redirect_uri = "http://localhost"
    client = DoubanClient(API_KEY, API_SECRET, your_redirect_uri, SCOPE)
    auth_code = "bbfda1b1ab14100633f8e515013c3012"

    # authorize
    print 'Go to the following link in your browser:'
    print client.authorize_url
    auth_code = raw_input('Enter the verification code:')

    # client.auth_with_code(auth_code)


    r = requests.post("https://www.douban.com/service/auth2/token",
                      data={"client_id": API_KEY, "client_secret": API_SECRET, "redirect_uri": your_redirect_uri,
                            "grant_type": "authorization_code", "code": auth_code})
    print r.json()
    access_token = r.json()["access_token"]

    # access_token = "bbfda1b1ab14100633f8e515013c3012"
    client.auth_with_code(access_token)

    # get current user
    # print client.user.me
    user = client.user.get("zilingqishi")
    print user

    # collection
    r = requests.post("https://api.douban.com/v2/book/20443559/collection", data={"status": "wish"})
    print r.json()

    # get movies of someone
    r = requests.post("https://api.douban.com/v2/movie/celebrity/1002667/works")
    print r.json()

    # get information of movies
    r = requests.post("https://api.douban.com/v2/movie/subject/1866473")
    print r.json()

__author__ = 'chenzhi'

import requests

if __name__ == "__main__":
    API_KEY = '0f2474e49ff2674d2d6d5eaddfd735e7'
    API_SECRET = 'ffc1f3ef21a0f872'

    USER = "douban_basic_common,community_basic_user"
    BOOK_SCOPE = "book_basic_r,book_basic_w,douban_basic_common"
    MOVIE_BASIC_SCOPE = "movie_basic_r,movie_basic_w"
    MOVIE_ADVANCED_SCOPE = "movie_advance_r,movie_advance_w"
    SCOPE = ",".join([USER, BOOK_SCOPE, MOVIE_ADVANCED_SCOPE, MOVIE_BASIC_SCOPE])

    your_redirect_uri = "http://localhost"

    """
    url = "https://www.douban.com/service/auth2/auth?client_id=%s&redirect_uri=%s&response_type=%s&scope=%s" % \
          (API_KEY, your_redirect_uri, "code", SCOPE)
    print "URL", url
    auth_code = raw_input('Enter the verification code:\n')
    print "auth_code", auth_code
    r = requests.post("https://www.douban.com/service/auth2/token",
                      data={"client_id": API_KEY, "client_secret": API_SECRET, "redirect_uri": your_redirect_uri,
                            "grant_type": "authorization_code", "code": auth_code})
    print r.json()
    access_token = r.json()["access_token"]
    print "access_token", access_token
    """

    access_token = "0de12a3fb65e504a29a37ebf231af0de"
    headers = {'Authorization': "Bearer " + access_token}

    # collection
    r = requests.post("https://api.douban.com/v2/book/26642172/collection", data={"status": "wish"}, headers=headers)
    print r.json()

    # get movies of someone
    # r = requests.get("https://api.douban.com/v2/movie/celebrity/1002667/works",  headers=headers)
    print r.json()


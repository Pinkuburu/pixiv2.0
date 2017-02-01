# -*- coding:utf-8 -*-

import requests
import re


def get_cookies(pid, password, text):
    s = requests.session()

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
     like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers1 = ({
        'Referer': 'https://accounts.pixiv.net/login?return_to=http%3A%2F%2F\
       www.pixiv.net%2Franking.php%3Fmode%3Ddaily&source=pc&view_type=page',
        'User-Agent': user_agent
    })

    shout_url = 'https://accounts.pixiv.net/login?return_to=http%3A%2F%2F\
    www.pixiv.net%2Franking.php%3Fmode%3Ddaily&source=pc&view_type=page'
    url1 = 'https://accounts.pixiv.net/api/login?lang=zh'

    res1 = s.get(shout_url, headers=headers1)

    content = res1.text
    pattern = re.compile('(?<=<input type="hidden" name="post_key" value=")\w*(?=">)')
    items = re.findall(pattern, content)
    if not items:
        print('postkey is not found')
        exit()
    postkey = items[0]

    data = ({
        'pixiv_id': str(pid),
        'password': str(password),
        'captcha': '',
        'g_recaptcha_response': '',
        'post_key': str(postkey),
        'source': 'pc'
    })

    s.post(url1, data=data)  # 登录页
    cookies = s.cookies
    fp = open(text, 'w')
    fp.write('; '.join(['='.join(item) for item in cookies.items()]))
    fp.close()  # 保存cookies
    print('save cookies is Success')


def loadcookie(text):
    loadcookies = {}
    f = open(text, 'r')
    for line in f.read().split(';'):
        name, value = line.strip().split('=', 1)
        loadcookies[name] = value
    f.close()
    print('load cookies is Success')
    return loadcookies

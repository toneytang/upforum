import requests
from bs4 import BeautifulSoup as bs
import time
import random

payload = {
    'username': 'wwww',
    'password': 'wwwww',
    'verifycode': '1111',
    'backurl': 'http://bbs.skykiwi.com/forum.php',
    'isRemember': '0'}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://passport.skykiwi.com/v1/login/bbslogon.do',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
    }

login_url = 'https://passport.skykiwi.com/v1/login/bbslogon.do'

s = requests.session()

r = s.post(login_url, headers=headers, params=payload)

print(r.text)
while True:
    thread_url_original = 'http://bbs.skykiwi.com/forum.php?mod=viewthread&tid=3941221'
    thread_url = 'http://bbs.skykiwi.com/forum.php?mod=post&action=reply&fid=33&tid=3941221&replysubmit=yes&infloat=yes&handlekey=fastpost&inajax=1'

    r = s.get(thread_url_original)
    soup = bs(r.text, 'html.parser',from_encoding='utf-8')
    formhash_value = soup.find_all('input',attrs = {'name':'formhash'})[0].get('value')
    thread_payload = {
        'message': 'ddddddddddddddddddddddddddddddddddd',
        'formhash': formhash_value,
        'usesig': '1',
        'subject': ''
        }
    #print(formhash_value)
    r = s.post(thread_url, params=thread_payload)

    print(r.text)
    sleep_seconds = random.randint(600, 3600)
    print('休息'+str(sleep_seconds)+'秒')
    time.sleep(sleep_seconds)

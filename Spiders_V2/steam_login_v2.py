# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/9/6--19:24
__author__ = 'Henry'

'''
Steam登录 (RSA加密)
网址:https://store.steampowered.com/login/
'''

import requests, execjs, time, re
import requests.cookies
from Spiders_V2 import qq_mail_recieve


def get_qqmail_captcha(email_address, email_password):
    '''
    获取QQ邮箱验证码
    :param email_address: 接收邮箱地址
    :param email_password: 接收邮箱的16位授权码
    :return: 收到的验证码
    '''
    content = qq_mail_recieve.recv_email_by_pop3(email_address, email_password)
    try:
        captcha = re.search(r'sans-serif; font-weight: bold;">(.*?)</span>', content).group(1)
        print('自动获取验证码成功!验证码为:' + captcha)
        return captcha
    except:
        print('自动获取验证码失败!')


def steam_login():
    '''登录函数'''
    req = requests.session()
    headers = {
        'Referer': 'https://store.steampowered.com/login/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    # 获取RSA公钥的了两个部分(mod 模数,exp 指数)
    url = 'https://store.steampowered.com/login/getrsakey/'
    data = {
        'donotcache': str(int(time.time() * 1000)),
        'username': user
    }
    html = req.post(url, data=data, headers=headers).json()
    print(html)
    pub_mod = html.get('publickey_mod')
    pub_exp = html.get('publickey_exp')
    timestamp = html.get('timestamp')
    # 加密密码
    with open('rsa.js', encoding='utf-8') as f:
        jsdata = f.read()
    passencrypt = execjs.compile(jsdata).call('getpwd', password, pub_mod, pub_exp)
    print(passencrypt)
    # 登录
    url = 'https://store.steampowered.com/login/dologin/'
    data = {
        'donotcache': str(int(time.time() * 1000)),
        'username': user,
        'password': passencrypt,
        'twofactorcode': '',
        'emailauth': '',
        'loginfriendlyname': '',
        'captchagid': '-1',
        'captcha_text': '',
        'emailsteamid': '',
        'rsatimestamp': timestamp,
        'remember_login': 'false',
    }
    html = req.post(url, data=data, headers=headers).json()
    print(html)
    if html.get('emailauth_needed') == True:
        print('登录需要您的QQ邮箱验证码...')
        emailid = html.get('emailsteamid')
        # email = input('[请输入您的QQ邮箱验证码:]')

        # 获取QQ邮箱验证码
        email_address = input('请输入Steam登录绑定的邮箱地址(eg:123456@qq.com):')
        email_password = input('请输入此绑定邮箱的16位授权码(eg:aaaabbbbccccdddd):')
        captcha = get_qqmail_captcha(email_address, email_password)

        # 带上验证码重新登录
        data['emailauth'] = captcha
        data['emailsteamid'] = emailid
        html = req.post(url, data=data, headers=headers).json()
        print(html)
        if html.get('login_complete') == True and html.get('success') == True:
            print('正在提交登录...')
            # 登录到个人中心
            # 方法一: 利用requests.cookies.update()函数添加新的cookie字段
            # 获取token,webcookie新的cookie字段
            steamid = html.get('transfer_parameters').get('steamid')
            token = html.get('transfer_parameters').get('token_secure')
            webcookie = html.get('transfer_parameters').get('webcookie')
            cookie = requests.cookies.RequestsCookieJar()
            cookie.set('steamLoginSecure', steamid + '%7C%7C' + token)
            cookie.set('steamMachineAuth', webcookie)
            req.cookies.update(cookie)  # 更新cookie
            url_store = 'https://store.steampowered.com/'
            html = req.get(url_store, headers=headers).text
            # print(html)
            username = re.findall(r'data-miniprofile=".*?">(.*?)</a>', html)[0]
            if username == user:
                print(req.cookies)
                print('登录成功!用户名为:' + username + '')

            # 方法二:一直保持session,就不用更新cookie了,直接请求即可
            # url_store = 'https://store.steampowered.com/'
            # html = req.get(url_store,headers=headers).text
            # print(html)
            # username = re.findall(r'data-miniprofile=".*?">(.*?)</a>',html)[0]
            # if username == user:
            #     print('[登录成功!用户名:' + username +']')

        else:
            print('登录失败!请重新登录!')
    elif html.get('success') == False and html.get('message') != '':
        print(html.get('message'))
        print('登录失败!请重新登录!')


if __name__ == '__main__':
    user = input('请输入您的steam账号:')
    password = input('请输入您的steam密码:')
    steam_login()

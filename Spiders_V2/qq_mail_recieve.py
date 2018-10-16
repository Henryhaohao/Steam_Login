# !/user/bin/env python
# -*- coding:utf-8 -*- 
# time: 2018/10/12--11:15
__author__ = 'Henry'

'''
QQ邮箱接收
'''

import poplib  # 邮件接收协议库


# 此函数通过使用poplib实现接收邮件
def recv_email_by_pop3(email_address, email_password):
    # 要进行邮件接收的邮箱。改成自己的邮箱
    # email_address = "your_email@qq.com"
    email_address = email_address
    # 要进行邮件接收的邮箱的16位授权码。改成自己的邮箱的16位授权码
    # email_password = "your_email_password"
    email_password = email_password
    # 邮箱对应的pop服务器，也可以直接是IP地址
    # 改成自己邮箱的pop服务器；qq邮箱不需要修改此值
    pop_server_host = "pop.qq.com"
    # 邮箱对应的pop服务器的监听端口。改成自己邮箱的pop服务器的端口；qq邮箱不需要修改此值
    pop_server_port = 995

    try:
        # 连接pop服务器。QQ邮箱接收需要使用ssl;如果没有使用SSL，将POP3_SSL()改成POP3()即可其他都不需要做改动
        email_server = poplib.POP3_SSL(host=pop_server_host, port=pop_server_port, timeout=10)
        print("[pop3--connect server success, now will check username]")
    except:
        print("[pop3--sorry the given email server address connect time out]")
        exit(1)
    try:
        # 验证邮箱是否存在
        email_server.user(email_address)
        print("[pop3--username exist, now will check password]")
    except:
        print("[pop3--sorry the given email address seem do not exist]")
        exit(1)
    try:
        # 验证邮箱密码是否正确
        email_server.pass_(email_password)
        print("[pop3--password correct,now will list email]")
        print('*' * 70)
        print('登录邮箱成功!正在获取验证码...')
    except:
        print("[pop3--sorry the given username seem do not correct]")
        exit(1)

    # stat()返回邮件数量和占用空间:
    # print('Messages: %s. Size: %s' % email_server.stat())
    # 邮箱中其收到的邮件的数量
    email_count = len(email_server.list()[1])
    # print('此邮箱中收件箱邮件数:' + str(email_count))
    # 通过retr(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
    resp, lines, octets = email_server.retr(email_count)
    # lines是邮件原始的内容(类似[b'1 82923', b'2 2184', ...])，列表形式使用join拼成一个byte变量
    email_content = b'\r\n'.join(lines)
    # 再将邮件内容由byte转成str类型
    email_content = email_content.decode()
    # print(email_content)
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接
    email_server.close()
    # 返回邮件内容,提供调用
    return email_content


if __name__ == '__main__':
    email_address = input('请输入要查询的邮箱地址(eg:123456@qq.com):')
    email_password = input('请输入要查询的邮箱16位授权码(eg:aaaabbbbccccdddd):')
    recv_email_by_pop3(email_address, email_password)

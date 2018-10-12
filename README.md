Python实现Steam游戏平台的模拟登录 ![enter image description here](Pic/logo.png)
===========================
![](https://img.shields.io/badge/Python-3.6.3-green.svg) ![](https://img.shields.io/badge/requests-2.18.4-green.svg) ![](https://img.shields.io/badge/PyExecJS-1.5.1-green.svg) 
### Steam游戏平台 - https://store.steampowered.com/
|Author|:sunglasses:Henryhaohao:sunglasses:|
|---|---
|Email|:hearts:1073064953@qq.com:hearts:

      
****
## :dolphin:声明
### 软件均仅用于学习交流，请勿用于任何商业用途！感谢大家！
## :dolphin:介绍
### 该项目为[Steam游戏平台](https://store.steampowered.com/)的模拟登录
- 项目版本:
> - 版本一:手动填写邮箱验证码进行登录:Spiders_V1
> - 版本二:自动获取邮箱验证码进行登录:Spiders_V2 (需用到python自带的poplib-邮件接收协议库并申请邮箱开启POP3/STMP服务;参考文章:https://www.cnblogs.com/lsdb/p/9419036.html;如何开启邮箱服务见下方截图)
- 爬虫文件:Spiders目录下的steam_login.py
- Password登录密码解密文件:Spiders目录下的rsa.js
## :dolphin:运行环境
Version: Python3
## :dolphin:安装依赖库
```
pip3 install -r requirements.txt
```
## :dolphin:**相关截图**
> - **Steam官网 - https://store.steampowered.com/**<br><br>
![enter image description here](Pic/steam.png)
> - **如何申请邮箱开启POP3/STMP服务**<br><br>
![enter image description here](Pic/1.png)
![enter image description here](Pic/2.png)
![enter image description here](Pic/3.png)
> - **Steam登录邮箱验证码样式**<br><br>
![enter image description here](Pic/4.png)
> - **运行过程(手动打码版本)**<br><br>
![enter image description here](Pic/run.png)
> - **运行过程(手动打码版本)**<br><br>
![enter image description here](Pic/run.png)
> - **运行过程(自动获取验证码版本)**<br><br>
![enter image description here](Pic/run_1.png)




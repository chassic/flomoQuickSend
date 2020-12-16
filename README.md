# Flomo Quick send 

Flomo Quick send client for windows using python

默认配置 windows键 + space 为全局快捷键，隐藏或显示，隐藏前自动发送消息



## 使用前准备

- 申请 Flomo 发送消息的 API https://flomoapp.com/mine?source=incoming_webhook

- 把 API 填写到 flomo.conf 文件

```
posturl= API
```



## 直接使用

- 安装 python 各种包

```
pip install configparser keyboard requests matplotlib pywin32
```

- python flomo.py



## 打包使用

- pip install py2exe
- python mysetup.py flomo.py
- 复制 flomo.ico flomo.conf 到生成目录


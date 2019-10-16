# 实验室资料库后端接口文档

[TOC]

## 环境要求

Windows/Linux

Python3.6+

## 安装方法

```
pip install -r requeirements.txt
```

## 目录结构

```
├── api 各路径接口存放目录
│    ├─user.py 
│    └─util.py
├── db 数据库相关文件目录
│    ├─Model 数据库模型
│    │   ├─UserRight.py
│    │   ├─UserAction.py
│    │   ├─Tag.py
│    │   ├─History.py
│    │   ├─Comment.py
│    │   ├─Article.py
│    │   └─User.py
│    ├─config.py 数据库配置文件
│    └─database.py 方法封装
├── util 常量、常用方法存放目录
│    ├─def_methods.py 常用方法文件
│    └─util.py 常量定义文件
├── main.py 入口文件
```

## 约定常量

### util/util.py

`REPLY_CODE_LIST`=Json code编码列表

`LOGIN_REQUIRED_LIST`=需要登陆验证的接口路径列表

`HOST`=服务器地址

`PORT`=服务端口

`DEBUG`=是否开启debug功能

### db/config.py

`USER_NAME`=数据库用户名

`PASSWORD`=数据库密码

`HOST_ADDRESS`=数据库地址

`PORT`=数据库端口

`DATABASE`=数据库名

`CHARSET`=字符集

## 常用封装方法

### 数据库操作 db.database

#### get_model(name)

- 描述：获取对应表格的模型对象
- 参数：
- 返回值：
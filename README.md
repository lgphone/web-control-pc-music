#### 背景

一个周末，10点起床，打开电脑，看了一会b站。

打开音乐软件(Foobar2000)，听音乐。躺到床上玩游戏，想换歌了,不想起床啊怎么办！！！

这时候我就花了一上午时间搞了个这个小玩意 :smile:

#### 原理
通过运行http服务 提供控制音乐及音量按钮

后端通过模拟键盘按下相关键进行控制

好吧就这么简单  :blush:

#### 使用
* 正在听歌
* 安装了 python 3.7
```shell script
git clone https://github.com/lgphone/web-control-pc-music.git
cd web-control-pc-music
python3 -m venv venv
source test_venv/Scripts/activate  # 不同系统命令不同 都是进入虚拟环境
pip install -r requirements.txt
python main.py
```

* 看到提示访问 ip:端口 使用手机浏览器打开即可

#### 界面预览
* 运行
![](https://github.com/lgphone/web-control-pc-music/blob/main/doc/pics/run.jpg)
* web
![](https://github.com/lgphone/web-control-pc-music/blob/main/doc/pics/web.jpg)
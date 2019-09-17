### Anki-Transtool

#### 作用
自动创建Anki中的英语单词卡片，音标和音频来自[韦氏词典](https://www.merriam-webster.com)，翻译来自[Google翻译](translate.google.cn),
按使用频率排序
> 只在macOS 10.14.6上使用过，其他平台自行测试
#### 配置
+ Anki安装Ankiconnect插件
+ Anki安装自己习惯的Markdown插件
+ 申请merriam-webster的app key，设置环境变量```MERRIAM_WEBSTER_KEY=<your key>```

#### 使用
```shell script
anki-transtool <word>
```


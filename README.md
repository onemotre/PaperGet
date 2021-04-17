# PaperGet -Improve Yourself

使用python爬虫技术爬取网上的高中学习资料，支持Windows系统

## 应用场景

- 用于高中生课下自行学习
- 教师查找资料，对之后的教学进行规划

## 操作提示

- 安装与运行
- 基本操作提示

### 软件的安装与运行

PaperGet是一款绿色软件，下载后直接循行`PaperGet.exe`文件即可

**第一次运行时需注意：**如果在菜单中勾选了**开始使用选项**，PaperGet会在当前的文件目录下创建`config.txt`文档用于储存*文件储存目录*（用于之后可以通过修改文件储存目录就可以文件下载路径）与`./题目`文件夹用于储存下载的文件，如果对文件的收集有特殊需求，可以将文件放置在合适的文件目录下，再自行创建快捷方式。

![Snipaste_2021-04-17_14-54-05](https://i.loli.net/2021/04/17/zT4QXcj1AebMhdF.png)

**特别提示：**本软件主要功能需要联网才能进行，且运行过程中不能使用VPN等网络代理工具

### 基本操作

- 找题做（选项a）

  - 学科的输入

    学科取高中主要学科的首字母，如：语文：YW

    PaperGet支持以下学科的资料爬取：语文、数学、英语、物理、化学、生物、政治、历史、地理、综合

  - 年级号的输入

    仅支持阿拉伯数字1-3的输入，分别对应高一、高二、高三。超过会提示输入错误，并需要重新输入所有信息

  - 文件数量的输入

    输入大于零的整数（1-9），一次性最好不要输入过多

    ![Snipaste_2021-04-17_15-02-01](https://i.loli.net/2021/04/17/irfNcg6QSeL8adG.png)

- 爬取后文件的查找

  所有文件都存放在`config.txt`文件中指示的对应位置，一般在执行文件目录下`题集`文件夹中

  - 关于`source.txt`文件

    该文件用于保存已经爬取了的文件的信息

    ![Snipaste_2021-04-17_15-05-19](https://i.loli.net/2021/04/17/RWN5e7Hpv4ZBclF.png)



### 更多帮助

本软件的试卷来自网站[高中试卷网](http://sj.smez.net/)

访问[PaperGet](https://github.com/onemotre/PaperGet)的github首页，获取后续版本更新

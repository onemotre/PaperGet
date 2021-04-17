# -*- coding = utf-8 -*-
# @Time :  19:55
# @Author : C_Studio
# @File : paperGet0.1.py
# @Software : PyCharm

import requests, re, os, time
from bs4 import BeautifulSoup

# 储存文件位置
FilePath = os.getcwd()
loc = [FilePath + '\\题集\\1语文', FilePath + '\\题集\\2数学', FilePath + '\\题集\\3英语', FilePath + '\\题集\\4物理', FilePath + '\\题集\\5化学', FilePath + '\\题集\\6生物', FilePath + '\\题集\\7政治', FilePath + '\\题集\\8历史', FilePath + '\\题集\\9地理', FilePath + '\\题集\\a综合']
subName = {'YW': '1语文', 'SX': '2数学', 'YY': '3英语', 'WL': '4物理', 'HX': '5化学', 'SW': '6生物', 'ZZ': '7政治', 'LS': '8历史', 'DL': '9地理', 'ZH': 'a综合'}
if not os.access(FilePath + '\\题集', os.F_OK):
    os.mkdir(FilePath + '\\题集')

# 正则表达式
# 找到下载界面引导界面
findDown_url = re.compile(str(r'<a href="(.*?)" target="_blank">'))
# 去除下载引导界面链接多余成分
delete = re.compile(str(r'amp;'))
# 找到下载链接
finddown_link = re.compile(str(r'<a href="(.*?)" title='))
# 找到文件的类型
docment_type = re.compile(str(r'http://sj.smez.net/.*?/\d{4}-\d{2}-\d{2}/(.*?)'))
docType = re.compile(str('.*?\.'))
# 信息处理
# 找到文件的id
docName = re.compile(str("/e/DownSys/DownSoft/\?classid=\d{1,3}&amp;id="))
# 文件的日期
dateFin = re.compile(str(r'<td align="center" nowrap="nowrap">\d{4}-\d{2}-\d{2}</td>'))

def main():
    initialization()
    cookie = login()  # 登陆信息
    os.system('cls')
    while 1:
        print('''
            PaperGet 0.1
            a.找题做
            b.开发者信息
            c.使用说明
            e.退出
            ''')
        choi = input()
        if choi == 'c':
            os.system('cls')
            print('''使用说明0.1\n前面的话
            1.选定exe可执行文件位置后请不要轻易改动, 这会导致你的电脑上有很多没用的文件与文件夹
            2.该版本为测试版, 开发者会在之后的更新中增加配置文件的功能
            使用中
            1.输入学科名称时为学科名称的首字母大写,如:语文-->YW (详情见下方)
            2.年级序数为阿拉伯数字, 仅支持1-9
            3.文件数量为一次性所爬取的文件数(一次不要爬取太多, 测试版本问题还很多, 在之后的版本中会逐渐修复)

            谢谢使用, 祝您生活愉快


            ''')
            for key, values in subName.items():
                print(values + '-->' + key)
            input("按任意键退出")
            os.system('cls')
        elif choi == 'b':
            os.system('cls')
            print('''开发者信息
            开发者:C_Studio
            反馈qq:2017786090
            ''')
            input("按任意键退出")
            os.system('cls')
        elif choi == 'a':
            while 1:
                subject = input("请输入学科:")
                grade = input("请输入年级号:")
                times = input("需要文件数量:")
                try:
                    times = int(times)
                    grade = int(grade)
                except ValueError as err:
                    os.system("cls")
                    print("输入有错误")
                    continue
                # 检查输入是否有错误
                if subject not in subName or grade < 1 or grade > 3:
                    os.system("cls")
                    print("输入有错误")
                else:
                    grade = str(grade)
                    break

            # 合成符合要求链接
            main_url = r'http://sj.smez.net/' + subject + r'/G' + grade

            # 开始下载
            downlod_url = DownloadPaper(main_url)
            for item in range(0, times):
                print("第%d份获取" % (item + 1))
                # print(main_url, item)
                tip = imformation(main_url, item)
                downlod_item = re.sub(delete, '', str(downlod_url[item]))
                downlod_item = r'http://sj.smez.net' + downlod_item  # 下载界面链接
                downlod_link = link(cookie, downlod_item)
                savePath(downlod_link, subject, tip)
            os.system("cls")

        elif choi == 'e':
            os.system("cls")
            break
        else:
            os.system("cls")
            print("输入错误")

# 初始化软件
def initialization():
    # 是否添加配置文件(储存文件储存位置)
    if not os.access(FilePath + str('\\confing.txt'), os.F_OK):
        print('''欢迎使用paperGet 0.1 \n
        ''')
        time.sleep(1)
        os.system('cls')

        while 1:
            choi = input("a.使用帮助; b.开始使用\n")
            if choi == 'a':
                print('''
                Thanks For Your Using \n
                1.请把该exe文件放置于用于储存资料的目录; 
                Note: 因为在这之后会生成名为\'confing.txt\'的文件, 同时用户也可以选择手动生成一个快捷方式 
                2.本软件需要进行联网进行; 

                ''')
                input("按任意键退出")
                os.system('cls')
            elif choi == 'b':
                for turn in loc:
                    os.mkdir(turn)
                break
            else:
                print("错误输入")

        # 创建配置文件
        f = open('./' + 'confing.txt', 'a')
        f.write("local1: \n")
        for turn in loc:
            f.write(turn + '\n')
        f.close()
        os.system('cls')

    # 已添加配置文件, 开始初始化文件夹(避免文件重复下载)
    print("初始化...")
    for turn in loc:
        if not os.path.exists(turn):
            os.mkdir(turn)
        if not os.access(turn + '\\' + str('1.sours.txt'), os.F_OK):
            f = open(turn + '/' + '1.sours.txt', 'a')
            f.write("目前已经拥有文件: ")
            f.close()

# 模拟登陆获取登陆cookie
def login():
    url = r'http://sj.smez.net/e/enews/index.php'
    data = {
            'enews': 'login',
            'ecmsfrom': '9',
            'username': '9938513',
            'password': '123456789',
            'Submit': '(unable to decode value)'
    }
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53"
    }
    req = requests.post(url=url, headers=head, data=data)
    cookies = requests.utils.dict_from_cookiejar(req.cookies)
    return cookies

def DownloadPaper(main_url):
    req = requests.get(url=main_url)
    html = req.text.encode("iso-8859-1").decode("GBK")
    soup = BeautifulSoup(html, "html.parser")
    item = str(soup.find_all('td', colspan="5"))
    url = re.findall(findDown_url, item)
    return url

def link(cookie, base_url):
    url = str(base_url)
    head = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53",
        "Accept": r"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
        "Referer": url,
        "Proxy-Connection": "keep-alive"
    }
    req = requests.post(url=url, headers=head, cookies=cookie)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    item = soup.find_all('td')
    downlink = re.findall(finddown_link, str(item))
    # print(downlink)

    # 将获取的链接中括号删除
    downlink = "".join(str(i) for i in downlink)
    # print(downlink)
    downlink = re.sub(delete, '', downlink)
    downlink = downlink.strip('../..')
    # 获取下载链接
    downlink = r'http://sj.smez.net/e/' + str(downlink)
    # print(downlink)
    return downlink

def savePath(downlink, subject, tips):
    req = requests.get(url=downlink)
    # print(type(req))
    name = req.url
    name = re.sub(docment_type, '', name)
    # print(name)
    filename = name
    name = re.sub(docType, '', name)
    file = FilePath + '\\题集\\' + subName[subject] + '\\'
    fi = open(file + '1.sours.txt', 'a')
    fi.write(str('\n') + str(filename))
    for tip in tips:
        fi.write('    ' + str(tip))
    fi.close()

    file = file + str(tips[2]) + '.' + name
    # print(file)
    with open(file, 'wb+') as f:
        f.write(req.content)
        f.close()

def imformation(downurl,turn):
    req = requests.get(url=downurl)
    html = req.text.encode("iso-8859-1").decode("GBK")
    soup = BeautifulSoup(html, "html.parser")
    # 获取当前页面的文件的id
    item = str(soup.find_all('td', colspan="5"))
    url = re.findall(findDown_url, item)
    # print(item, url)
    # 获取文件id
    i = 0
    allId = []
    for idNumTurn in url:
        idNum = re.sub(docName, '', idNumTurn)
        idNum = re.sub(re.compile(str(r'&amp;pathid=\d{1}')), '', idNum)
        allId.insert(i, idNum) # 列表的增加需要用insert
        # print(allId)
        i = i + 1
    # print(allId)
    # 获取文件日期date
    date = str(soup.find_all('td', align="center"))
    date = re.findall(dateFin, date)
    # print(date[2])
    date1 = []
    for a in range(0,len(date)):
        # print(date[a])
        item1 = re.sub(re.compile(str(r'<td align="center" nowrap="nowrap">')), '', date[a])
        item1 = re.sub(re.compile(str(r'</td>')), '', item1)
        date1.insert(a, item1)
    # print(date1)
    imforUrl = downurl + '/' + date1[turn] + '/' + allId[turn] + r'.html'
    pap = requests.get(url = imforUrl)
    html2 = pap.text.encode("iso-8859-1").decode('GBK')
    soup2 = BeautifulSoup(html2, 'html.parser')

    # 获取试卷类型
    item = str(soup2.find_all('td', width="200"))
    papType = re.sub(re.compile(r'\[<td width="200">'), '', item)
    papType = re.sub(re.compile(r'</td>(.*)'), '', papType)
    papType = "".join(papType)

    # 获取适用学期
    item2 = str(soup2.find_all('td', width="350"))
    fitJob = re.findall(re.compile(str(r'适用学期：</strong>.*?</td>')), item2)
    fitJob = re.sub(re.compile(str(r'</strong>')), '', str(fitJob))
    fitJob = re.sub(re.compile(str(r'</td>')), '', str(fitJob))

    # 获取试卷名称
    item3 = str(soup2.find_all('td', colspan="3"))
    name = re.findall(re.compile(str(r'<b>.*?</b>')), item3)
    name = re.sub(re.compile('<b>'), '', name[0])
    name = re.sub(re.compile('</b>'), ' ', name)

    return papType, fitJob, name


if __name__ == '__main__':
    main()
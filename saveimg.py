# -*- coding:utf-8 -*-
import requests
import re
import os
import asyncio
import time

user_agent = 'User-Agent,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers1 = ({
    'Referer': 'http://www.pixiv.net/',
    'User-Agent': user_agent
})
msg1 = 'is too long'
msg2 = ' may gif'
filename1 = 'long picid.txt'
filename2 = 'gifid.txt'

def reget(p, dataidurl, s):
    try:
        res = s.get(dataidurl)  # 相应id网站
        return res
    except:
        try:
            if p.detail:
                print('try again')
            time.sleep(3)
            res = s.get(dataidurl)  # 相应id网站
            return res
        except:
            if p.detail:
                print('connect error')
            #sys.exit()
            return 0

def writetxt(path,str,msg,filename):
    print(str+msg)
    ft = open(path+'\\'+filename,'a')    #将图id号输出到txt，以便自行查看
    ft.write(str+'\n')
    ft.close

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    is_exists = os.path.exists(path)
    if not is_exists:  # 如果不存在则创建目录
        print(path + ' Success')   # 创建目录操作函数
        os.makedirs(path)
        return True
    else:  # 如果目录存在则不创建，并提示目录已存在
        print(path + ' existence')
        return False


def save(number, dataids, cookies, path, ceiling=4):
    i = 0
    number = number
    s = requests.session()
    s.cookies = requests.utils.cookiejar_from_dict(cookies)
    s.headers = headers1
    #print(ceiling)
    while i < number:
        b = 0
        dataidurl = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + str(dataids[i])
        #res1 = requests.get(url=dataidurl, cookies=cookies,
          #                  headers=headers1)  # 相应id网站
        # try:
        #         res1 = s.get(dataidurl)  # 相应id网站
        # except:
        #     try:
        #         print('try again')
        #         time.sleep(3)
        #         res1 = s.get(dataidurl)  # 相应id网站
        #     except:
        #         print('connect error')
        res1 = reget(dataidurl,s)
        content1 = res1.text
        pattern1 = re.compile('(?<= data-src=")\S*(?=" class="original-image">)')
        originaltus = re.findall(pattern1, content1)
        if not originaltus:
            dataidurl = 'http://www.pixiv.net/member_illust.php?mode=manga&illust_id=' + str(dataids[i])
            #res2 = requests.get(url=dataidurl, cookies=cookies,
             #                   headers=headers1)  # 相应id网站
            # try:
            #     res2 = s.get(dataidurl)  # 相应id网站
            # except:
            #     try:
            #         print('try again')
            #         time.sleep(3)
            #         res2 = s.get(dataidurl)  # 相应id网站
            #     except:
            #         print('connect error')
            res2 = reget(dataidurl,s)
            content2 = res2.text
            pattern2 = re.compile('(?<=data-filter="manga-image" data-src=")\S*(?=" data-index)')
            originaltus = re.findall(pattern2, content2)
            if not originaltus:
                writetxt(path,str(i),msg2,filename2)
                i += 1
                continue

        for originaltu in originaltus:
            b += 1
        if b >= ceiling:
            print(str(dataids[i])+' is too long')
            i += 1
            continue
        else:
            b = 0  # 判断id图片是否过多

        for originaltu in originaltus:
            content3 = originaltu
            pattern3 = re.compile('png')
            ifpng = re.findall(pattern3, content3)
            if not ifpng:
                    str1 = 'jpg'
            else:
                    str1 = 'png'  # 判断后缀是jpg还是png
            '''print(dataids[i] +'-'+str(b)+ ' is downloading')'''
            string = 'pixiv' + str(dataids[i]) + '-' + 'p' + str(b) + '.' + str1
            if is_exists:
                filesize = os.path.getsize(path+'\\'+string)
                if filesize == 0:
                    os.remove(path+'\\'+string)
                    is_exists = False
                elif str1 == 'jpg':
                    f = open(path+'\\'+string, 'rb')
                    f.seek(-2, 2)
                    if f.read() != '\xff\xd9':
                        f.close()
                        os.remove(path+'\\'+string)
                        is_exists = False
                    else:
                        f.close()
                else:
                    pass
            if not is_exists:
                pic = requests.get(originaltu, stream=True, cookies=cookies, headers=headers1)
                fp = open(path + '\\' + string, 'wb')
                fp.write(pic.content)
                fp.close()  # 保存图片
                '''print(dataids[i]+'-'+str(b) + ' download is Success')'''
                b += 1
            else:
                b += 1
        i += 1

    if number == 0:
        if len(dataids) > 30:
            print('All Download')
        for i in dataids:
            b = 0
            dataidurl = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + str(i)
            # res1 = s.get(dataidurl)  # 相应id网站
            res1 = reget(dataidurl,s)
            content1 = res1.text
            pattern1 = re.compile('(?<= data-src=")\S*(?=" class="original-image">)')
            originaltus = re.findall(pattern1, content1)
            if not originaltus:
                print('pic grp')
                dataidurl = 'http://www.pixiv.net/member_illust.php?mode=manga&illust_id=' + str(i)
                # res2 = s.get(dataidurl)  # 相应id网站
                res2 = reget(dataidurl,s)
                content2 = res2.text
                pattern2 = re.compile('(?<=data-filter="manga-image" data-src=")\S*(?=" data-index)')
                originaltus = re.findall(pattern2, content2)
                if not originaltus:
                    # print(str(i) + 'may gif')
                    # ft = open(path+'\\'+'gifid.txt','a')    #将gif图 id号输出到txt，以便自行查看
                    # ft.write(str(i)+'\n')
                    # ft.close
                    writetxt(path,str(i),msg2,filename2)
                    continue

            for originaltu in originaltus:
                b += 1
            if b >= ceiling:
                # print(str(i)+' is too long')
                # ft = open(path+'\\'+'long picid.txt','a')    #将过长的组图id号输出到txt，以便自行查看
                # ft.write(str(i)+'\n')
                # ft.close
                writetxt(path,str(i),msg1,filename1)
                continue
            else:
                b = 0  # 判断id图片是否过多

            for originaltu in originaltus:
                content3 = originaltu
                pattern3 = re.compile('png')
                ifpng = re.findall(pattern3, content3)
                if not ifpng:
                        str1 = 'jpg'
                else:
                        str1 = 'png'  # 判断后缀是jpg还是png
                '''print(i +'-'+str(b)+ ' is downloading')'''
                string = 'pixiv' + str(i) + '-' + 'p' + str(b) + '.' + str1
                is_exists = os.path.exists(path+'\\'+string)
                '''if is_exists:
                    filesize = os.path.getsize(path+'\\'+string)
                    if filesize == 0:
                        os.remove(path+'\\'+string)
                        is_exists = False
                    elif str1 == 'jpg':
                        f = open(path+'\\'+string, 'rb')
                        f.seek(-2, 2)
                        if f.read() != '\xff\xd9':
                            f.close()
                            os.remove(path+'\\'+string)
                            is_exists = False
                        else:
                            f.close()
                    else:
                        pass'''
                if not is_exists:
                    try:
                        pic = s.get(originaltu, timeout=180)
                        fp = open(path + '\\' + string, 'wb')
                        fp.write(pic.content)
                        fp.close()  # 保存图片
                        print(i+'-'+str(b) + ' download is Success')
                        b += 1
                    except requests.exceptions.ConnectionError:
                        print('Read timed out.')
                else:
                    b += 1

async def simgle_async_save(i, path, ceiling=4):
    b = 0
    dataidurl = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + str(i)
    res1 = await get(dataidurl)  # 相应id网站
    content1 = res1.text
    pattern1 = re.compile('(?<= data-src=")\S*(?=" class="original-image">)')
    originaltus = re.findall(pattern1, content1)
    if not originaltus:
        dataidurl = 'http://www.pixiv.net/member_illust.php?mode=manga&illust_id=' + str(i)
        res2 = await get(dataidurl)  # 相应id网站
        content2 = res2.text
        pattern2 = re.compile('(?<=data-filter="manga-image" data-src=")\S*(?=" data-index)')
        originaltus = re.findall(pattern2, content2)
        if not originaltus:
            writetxt(path,str(i),msg2,filename2)
            return 0

    for originaltu in originaltus:
        b += 1
    if b >= ceiling:
        #print(str(i)+' is too long')
        writetxt(path,str(i),msg1,filename1)
        return 0
    else:
        b = 0  # 判断id图片是否过多

    for originaltu in originaltus:
        content3 = originaltu
        pattern3 = re.compile('png')
        ifpng = re.findall(pattern3, content3)
        if not ifpng:
                str1 = 'jpg'
        else:
                str1 = 'png'  # 判断后缀是jpg还是png
        '''print(i +'-'+str(b)+ ' is downloading')'''
        string = 'pixiv' + str(i) + '-' + 'p' + str(b) + '.' + str1
        is_exists = os.path.exists(path+'\\'+string)
        '''if is_exists:
            filesize = os.path.getsize(path+'\\'+string)
            if filesize == 0:
                os.remove(path+'\\'+string)
                is_exists = False
            elif str1 == 'jpg':
                f = open(path+'\\'+string, 'rb')
                f.seek(-2, 2)
                if f.read() != '\xff\xd9':
                    f.close()
                    os.remove(path+'\\'+string)
                    is_exists = False
                else:
                    f.close()
            else:
                pass'''
        if not is_exists:
            pic = await get(originaltu)
            fp = open(path + '\\' + string, 'wb')
            fp.write(pic.content)
            fp.close()  # 保存图片
            '''print(i+'-'+str(b) + ' download is Success')'''
        else:
            pass

loop = asyncio.get_event_loop()
s = requests.session()
# s.cookies = requests.utils.cookiejar_from_dict(cookies)
s.headers = headers1


def get2(url, asession=s):
    return asession.get(url, timeout=180)


def get(url):
    return loop.run_in_executor(None, get2, url)


def async_save(dataids, cookies, path):
    s.cookies = requests.utils.cookiejar_from_dict(cookies)
    tasks = []
    while dataids:
        if len(dataids) <= 30:
            for i in dataids:
                tasks.append(simgle_async_save(i, path))
                dataids.remove(i)
            loop.run_until_complete(asyncio.wait(tasks))
            tasks = []
        else:
            for i in dataids[:30]:
                tasks.append(simgle_async_save(i, path))
                dataids.remove(i)
            loop.run_until_complete(asyncio.wait(tasks))
            tasks = []
    loop.close()
    return 0

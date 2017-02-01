# -*- coding:utf-8 -*-
import re
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 \
Safari/537.36'
headers1 = ({
    'Referer': 'http://www.pixiv.net/',
    'User-Agent': user_agent
})


def getid(keyword, cookies, r18=False, leastpages=100, leastlikes=1000, startpage=0):
    baseurl = r18c('http://www.pixiv.net/search.php?word=' + keyword_swich(keyword), r18)
    dataids = []
    for i in range(startpage, leastpages):
        myurl = baseurl + '&p=' + str(i+1)
        html = requests.get(url=myurl, cookies=cookies, headers=headers1).text
        targetlist = re.findall(u'<a href="/bookmark_detail\.php\?illust_id=\d+" class="bookmark-count _ui-tooltip" '
                                u'data-tooltip="[0-9,]+', html)
        if not targetlist:
            print('Page %d is Empty' % (i+1))
            return dataids
        for j in targetlist:
            img_id = re.search('id=\d+', j).group()[3:]
            likenumber = int(re.search('"[0-9,]+', j).group()[1:].replace(',', ''))
            if likenumber >= leastlikes:
                dataids.append(img_id)
        print('Page %d is Done' % (i+1))
    return dataids


def r18c(url, r18=False):
    if r18:
        url += '&r18=1'
        return url
    else:
        url += '&r18=0'
        return url


def keyword_swich(keyword):
    byte = keyword
    Dbytedir = {b'\x00':'%00',b'\x01':'%01',b'\x02':'%02',b'\x03':'%03',b'\x04':'%04',b'\x05':'%05',b'\x06':'%06',b'\x07':'%07',b'\x08':'%08',b'\x09':'%09',b'\x0a':'%0A',b'\x0b':'%0B',b'\x0c':'%0C',b'\x0d':'%0D',b'\x0e':'%0E',b'\x0f':'%0F',b'\x10':'%10',b'\x11':'%11',b'\x12':'%12',b'\x13':'%13',b'\x14':'%14',b'\x15':'%15',b'\x16':'%16',b'\x17':'%17',b'\x18':'%18',b'\x19':'%19',b'\x1a':'%1A',b'\x1b':'%1B',b'\x1c':'%1C',b'\x1d':'%1D',b'\x1e':'%1E',b'\x1f':'%1F',b'\x20':'%20',b'\x21':'%21',b'\x22':'%22',b'\x23':'%23',b'\x24':'%24',b'\x25':'%25',b'\x26':'%26',b'\x27':'%27',b'\x28':'%28',b'\x29':'%29',b'\x2a':'%2A',b'\x2b':'%2B',b'\x2c':'%2C',b'\x2d':'%2D',b'\x2e':'%2E',b'\x2f':'%2F',b'\x30':'%30',b'\x31':'%31',b'\x32':'%32',b'\x33':'%33',b'\x34':'%34',b'\x35':'%35',b'\x36':'%36',b'\x37':'%37',b'\x38':'%38',b'\x39':'%39',b'\x3a':'%3A',b'\x3b':'%3B',b'\x3c':'%3C',b'\x3d':'%3D',b'\x3e':'%3E',b'\x3f':'%3F',b'\x40':'%40',b'\x41':'%41',b'\x42':'%42',b'\x43':'%43',b'\x44':'%44',b'\x45':'%45',b'\x46':'%46',b'\x47':'%47',b'\x48':'%48',b'\x49':'%49',b'\x4a':'%4A',b'\x4b':'%4B',b'\x4c':'%4C',b'\x4d':'%4D',b'\x4e':'%4E',b'\x4f':'%4F',b'\x50':'%50',b'\x51':'%51',b'\x52':'%52',b'\x53':'%53',b'\x54':'%54',b'\x55':'%55',b'\x56':'%56',b'\x57':'%57',b'\x58':'%58',b'\x59':'%59',b'\x5a':'%5A',b'\x5b':'%5B',b'\x5c':'%5C',b'\x5d':'%5D',b'\x5e':'%5E',b'\x5f':'%5F',b'\x60':'%60',b'\x61':'%61',b'\x62':'%62',b'\x63':'%63',b'\x64':'%64',b'\x65':'%65',b'\x66':'%66',b'\x67':'%67',b'\x68':'%68',b'\x69':'%69',b'\x6a':'%6A',b'\x6b':'%6B',b'\x6c':'%6C',b'\x6d':'%6D',b'\x6e':'%6E',b'\x6f':'%6F',b'\x70':'%70',b'\x71':'%71',b'\x72':'%72',b'\x73':'%73',b'\x74':'%74',b'\x75':'%75',b'\x76':'%76',b'\x77':'%77',b'\x78':'%78',b'\x79':'%79',b'\x7a':'%7A',b'\x7b':'%7B',b'\x7c':'%7C',b'\x7d':'%7D',b'\x7e':'%7E',b'\x7f':'%7F',b'\x80':'%80',b'\x81':'%81',b'\x82':'%82',b'\x83':'%83',b'\x84':'%84',b'\x85':'%85',b'\x86':'%86',b'\x87':'%87',b'\x88':'%88',b'\x89':'%89',b'\x8a':'%8A',b'\x8b':'%8B',b'\x8c':'%8C',b'\x8d':'%8D',b'\x8e':'%8E',b'\x8f':'%8F',b'\x90':'%90',b'\x91':'%91',b'\x92':'%92',b'\x93':'%93',b'\x94':'%94',b'\x95':'%95',b'\x96':'%96',b'\x97':'%97',b'\x98':'%98',b'\x99':'%99',b'\x9a':'%9A',b'\x9b':'%9B',b'\x9c':'%9C',b'\x9d':'%9D',b'\x9e':'%9E',b'\x9f':'%9F',b'\xa0':'%A0',b'\xa1':'%A1',b'\xa2':'%A2',b'\xa3':'%A3',b'\xa4':'%A4',b'\xa5':'%A5',b'\xa6':'%A6',b'\xa7':'%A7',b'\xa8':'%A8',b'\xa9':'%A9',b'\xaa':'%AA',b'\xab':'%AB',b'\xac':'%AC',b'\xad':'%AD',b'\xae':'%AE',b'\xaf':'%AF',b'\xb0':'%B0',b'\xb1':'%B1',b'\xb2':'%B2',b'\xb3':'%B3',b'\xb4':'%B4',b'\xb5':'%B5',b'\xb6':'%B6',b'\xb7':'%B7',b'\xb8':'%B8',b'\xb9':'%B9',b'\xba':'%BA',b'\xbb':'%BB',b'\xbc':'%BC',b'\xbd':'%BD',b'\xbe':'%BE',b'\xbf':'%BF',b'\xc0':'%C0',b'\xc1':'%C1',b'\xc2':'%C2',b'\xc3':'%C3',b'\xc4':'%C4',b'\xc5':'%C5',b'\xc6':'%C6',b'\xc7':'%C7',b'\xc8':'%C8',b'\xc9':'%C9',b'\xca':'%CA',b'\xcb':'%CB',b'\xcc':'%CC',b'\xcd':'%CD',b'\xce':'%CE',b'\xcf':'%CF',b'\xd0':'%D0',b'\xd1':'%D1',b'\xd2':'%D2',b'\xd3':'%D3',b'\xd4':'%D4',b'\xd5':'%D5',b'\xd6':'%D6',b'\xd7':'%D7',b'\xd8':'%D8',b'\xd9':'%D9',b'\xda':'%DA',b'\xdb':'%DB',b'\xdc':'%DC',b'\xdd':'%DD',b'\xde':'%DE',b'\xdf':'%DF',b'\xe0':'%E0',b'\xe1':'%E1',b'\xe2':'%E2',b'\xe3':'%E3',b'\xe4':'%E4',b'\xe5':'%E5',b'\xe6':'%E6',b'\xe7':'%E7',b'\xe8':'%E8',b'\xe9':'%E9',b'\xea':'%EA',b'\xeb':'%EB',b'\xec':'%EC',b'\xed':'%ED',b'\xee':'%EE',b'\xef':'%EF',b'\xf0':'%F0',b'\xf1':'%F1',b'\xf2':'%F2',b'\xf3':'%F3',b'\xf4':'%F4',b'\xf5':'%F5',b'\xf6':'%F6',b'\xf7':'%F7',b'\xf8':'%F8',b'\xf9':'%F9',b'\xfa':'%FA',b'\xfb':'%FB',b'\xfc':'%FC',b'\xfd':'%FD',b'\xfe':'%FE',b'\xff':'%FF'}
    result = ''
    for i in range(len(byte)):
        target = byte[i:i+1]
        result = result + Dbytedir.get(target)
    return result

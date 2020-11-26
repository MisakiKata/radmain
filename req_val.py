#coding:utf-8


import requests
import difflib
import configparser
import logging

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
cookie2 = config['cookie']['cookie2']
cookie3 = config['cookie']['cookie3']
cookie4 = config['cookie']['cookie4']
similar = config['simil']['site']
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class REQ:
    def __init__(self, url, header, body):
        self.url = url
        self.header = header
        self.body = body

    def getreq(self):
        val_js = {}
        r = requests.get(url=self.url, headers=self.header)

        if cookie2 != '':
            self.header['Cookie'] = cookie2
            r2 = requests.get(url=self.url, headers=self.header)
            simi = difflib.SequenceMatcher(None, r.text, r2.text).quick_ratio()
            if simi >= float(similar):
                logging.info('存在范围内的请求，权限Cookie2.相似度：%s' %str(simi))
                val_js['url'] = self.url
                val_js['header'] = self.header

        if cookie3 != '':
            self.header['Cookie'] = cookie3
            r2 = requests.get(url=self.url, headers=self.header)
            simi = difflib.SequenceMatcher(None, r.text, r2.text).quick_ratio()
            if simi >= float(similar):
                logging.info('存在范围内的请求，权限Cookie3.相似度：%s' %str(simi))
                if 'header' in val_js.keys():
                    val_js['header2'] = self.header
                else:
                    val_js['url'] = self.url
                    val_js['header'] = self.header

        if cookie4 != '':
            self.header['Cookie'] = cookie4
            r2 = requests.get(url=self.url, headers=self.header)
            simi = difflib.SequenceMatcher(None, r.text, r2.text).quick_ratio()
            if simi >= float(similar):
                logging.info('存在范围内的请求，权限Cookie4.相似度：%s' %str(simi))
                if 'header' in val_js.keys() or 'header2' in val_js.keys():
                    val_js['header3'] = self.header
                else:
                    val_js['url'] = self.url
                    val_js['header'] = self.header

        return val_js

    def postreq(self):
        val_js = {}
        r = requests.post(url=self.url, headers=self.header, data=self.body)

        if cookie2 != '':
            self.header['Cookie'] = cookie2
            r2 = requests.post(url=self.url, headers=self.header, data=self.body)
            simi = difflib.SequenceMatcher(None, r.text, r2.text).quick_ratio()
            if simi >= float(similar):
                logging.info('存在范围内的请求，权限Cookie2.相似度：%s' %str(simi))
                val_js['url'] = self.url
                val_js['header'] = self.header
                val_js['body'] = self.body

        if cookie3 != '':
            self.header['Cookie'] = cookie3
            r2 = requests.post(url=self.url, headers=self.header, data=self.body)
            simi = difflib.SequenceMatcher(None, r.text, r2.text).quick_ratio()
            if simi >= float(similar):
                logging.info('存在范围内的请求，权限Cookie3.相似度：%s' %str(simi))
                if 'header' in val_js.keys():
                    val_js['header2'] = self.header
                else:
                    val_js['url'] = self.url
                    val_js['header'] = self.header
                    val_js['body'] = self.body

        if cookie4 != '':
            self.header['Cookie'] = cookie4
            r2 = requests.post(url=self.url, headers=self.header, data=self.body)
            simi = difflib.SequenceMatcher(None, r.text, r2.text).quick_ratio()
            if simi >= float(similar):
                logging.info('存在范围内的请求，权限Cookie4.相似度：%s' %str(simi))
                if 'header' in val_js.keys() or 'header2' in val_js.keys():
                    val_js['header3'] = self.header
                else:
                    val_js['url'] = self.url
                    val_js['header'] = self.header
                    val_js['body'] = self.body

        return val_js
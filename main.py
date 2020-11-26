# This is a sample Python script.

from spider import spider
import json
import configparser
import base64
import logging
from req_val import REQ


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
cookie = config['cookie']['cookie']
page = config['page']['url']
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def origer(method, url, header, body):
    req = REQ(url=url, header=header, body=str(body, encoding='utf-8'))
    if method == 'GET':
        text = str(req.getreq())
        if text != {}:
            logging.info('存在以下请求：' + text)
    elif method == 'POST':
        text = str(req.postreq())
        if text != {}:
            logging.info('存在以下请求：' + text)

def readfile(page, cookie):
    sp = spider(page, cookie)
    with open(sp.main(), 'r', encoding='utf-8') as f:
        for req in json.loads(f.read()):
            method = req['Method']
            url = req['URL']
            header = req['Header']
            body = b''
            logging.info(url)
            if 'b64_body' in req.keys():
                body = base64.b64decode(bytes(req['b64_body'], encoding='utf-8'))
            origer(method, url, header, body)


if __name__ == '__main__':
    readfile(page, cookie)


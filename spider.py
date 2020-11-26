#coding:utf-8

import subprocess
import os
import logging

rad = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rad\\rad.exe')
radir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rad\\result.json')
radcof = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rad\\rad_config.yml')
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(levelname)s - %(message)s')


class spider:

    def __init__(self, page, cookie):
        self.page = page
        self.cookie = cookie


    def conf(self):
        name = self.cookie.split('=')[0]
        value = self.cookie.split('=')[1]
        radyam = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rad\\rad_config.yml.sample')
        f = open(radyam, encoding='utf-8')
        conf = f.read().replace('$NAME$', name).replace('$VALUE$', value).replace('$URL$', self.page)
        f.close()
        with open(radcof, 'w', encoding='utf-8') as ff:
            ff.write(conf)
        logging.info('配置文件处理完成')


    def serv_info(self):
        self.jsonf()
        sub = subprocess.Popen([rad, '-t', self.page, '-json', radir, '-c', radcof], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stdout, stderr = sub.communicate()
        logging.info(str(stdout, encoding='utf-8'))
        if stderr != b'':
            logging.warning(stderr)
            return stderr
        return radir

    def jsonf(self):
        if os.path.exists(radir):
            os.remove(radir)
        if os.path.exists(radcof):
            os.remove(radcof)
        self.conf()

    def main(self):
        if os.path.isfile(self.serv_info()):
            logging.info('执行完毕，文件保存：' + radir)
            return radir
        else:
            logging.warning(str(self.serv_info(), encoding='utf-8'))
            os._exit()


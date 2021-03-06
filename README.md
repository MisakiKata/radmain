  <h3 align="center">越权检测</h3>

## 目录

* [关于项目](#关于项目)
* [使用](#使用)
* [描述](#描述)
* [License](#license)

## 关于项目

看过之前的一些脚本和bp的插件，被动或者扫描代理流量的方式来检测，所以就想是否可以主动测试，正好rad可以采集地址和参数，于是就有这个尝试。

一个简单的越权检测，主动式，采用的方法是使用rad爬取连接，然后替换其中的cookie，然后判断页面返回的相似度来检测是否成功。需要测试的地址和cookie在config.ini中配置。

## 使用

rad: https://github.com/chaitin/rad

```sh
由于rad需要谷歌浏览，所以需要事先安装，如果浏览器没有配置PATH，需要设置exec-path地址

需要配置地址，如果是后台需要设置登陆后的后台地址
[page]
# shouye
url = http://testphp.vulnweb.com

在cookie设置中，第一个cookie为rad采集的cookie，一般设置高权限，其他的根本需要设置需要的权限即可。
相似度默认为0.8，设置为0-1.0的值，类型float。

rad目录下有生成的采集文件，如果检测不正常可以查看文件是否采集正常。如果需要设置rad的配置，修改目录下的rad_config.yml.sample文件，后续的配置文件根据此修改来。

run: python3 main.py
```

## 描述

配置后，rad会自动检测采集地址，然后交给程序更改权限后访问，根据相似度来判断输出，相似度设置高则误报少漏报高，设置低漏报少误报高。

在测试中发现有些rad采集不到地址的情况，这种情况大都存在超链接js加载。这时候采集不到，自然也不能测试。所以受到rad采集的限制，建议此工具辅助使用。

## License

GPL-2.0 © 2020 Misakikata

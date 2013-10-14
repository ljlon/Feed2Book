#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from base import BaseFeedBook

def getBook():
    return Songshuhui

class Songshuhui(BaseFeedBook):
    title                 = u'科学松鼠会'
    description           = u'科学松鼠会是一个汇聚了当代最优秀的华语青年科学传播者的非营利机构，旨在“剥开科学的坚果，帮助人们领略科学之美妙'
    category              = 1
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    network_timeout       = 30
    fetch_img_via_ssl     = False
    feeds = [
            (u'科学松鼠会', 'http://songshuhui.net/feed', True),
           ]
           
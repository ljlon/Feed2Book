#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from base import BaseFeedBook

def getBook():
    return BBCChina

class BBCChina(BaseFeedBook):
    title                 = u'BBC中文网'
    description           = u'BBC中文网'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    network_timeout       = 30
    fetch_img_via_ssl     = False
    feeds = [
            (u'BBC中文网', 'http://www.bbc.co.uk/zhongwen/simp/index.xml'),
           ]
           
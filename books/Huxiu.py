#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from base import BaseFeedBook

def getBook():
    return Huxiu

class Huxiu(BaseFeedBook):
    title                 = u'虎嗅'
    description           = u'虎嗅网是一个有视角的、个性化商业资讯与交流平台，核心关注对象是包括公众公司与创业型企业在内的一系列明星公司.'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    network_timeout       = 30
    fetch_img_via_ssl     = False
    feeds = [
            (u'虎嗅', 'http://www.huxiu.com/rss/0.xml'),
           ]
           
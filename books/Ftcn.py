#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from base import BaseFeedBook

def getBook():
    return FtCN

class FtCN(BaseFeedBook):
    title                 = u'FT中文网_英国《金融时报》'
    description           = u'FT中文网每日新闻'
    category              = 2
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    network_timeout       = 30
    fetch_img_via_ssl     = False
    feeds = [
            (u'FT中文网每日新闻', 'http://www.ftchinese.com/rss/feed'),
           ]
           
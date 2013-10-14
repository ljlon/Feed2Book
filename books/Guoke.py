#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from base import BaseFeedBook

def getBook():
    return Guoke

class Guoke(BaseFeedBook):
    title                 = u'果壳网'
    description           = u'果壳网是一个泛科技主题网站，提供负责任、有智趣、贴近生活的内容，你可以在这里阅读、分享、交流、提问。果壳网致力于让科技兴趣成为人们文化生活和娱乐生活的重要元素'
    category              = 1
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    network_timeout       = 30
    fetch_img_via_ssl     = False
    feeds = [
            (u'果壳网', 'http://www.guokr.com/rss/', True),
           ]
           
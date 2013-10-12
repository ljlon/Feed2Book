#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from base import BaseFeedBook

def getBook():
    return Douban

class Douban(BaseFeedBook):
    title                 = u'豆瓣'
    description           = u'豆瓣最受欢迎的影评'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    network_timeout       = 30
    fetch_img_via_ssl     = False
    feeds = [
            (u'豆瓣最受欢迎的影评', 'http://movie.douban.com/feed/review/movie'),
           ]
           
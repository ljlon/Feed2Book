#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

_booksclasses = []
_bookcategoryclasses = []

def RegisterBook(book):
    if book.title:
        _booksclasses.append(book)

def BookClasses():
    return _booksclasses

def BookClass(title):
    for bk in _booksclasses:
        if bk.title == title:
            return bk
    return None

def LoadBooks():
    for bkfile in os.listdir(os.path.dirname(__file__)):
        if bkfile.endswith('.py') and not bkfile.startswith('__') and not bkfile.endswith("base.py"):
            bookname = os.path.splitext(bkfile)[0]
            try:
                mbook = __import__("books." + bookname, fromlist='*')
                bk = mbook.getBook()
                #globals()[bk.__name__] = getattr(bk, bk.__name__)
                RegisterBook(bk)
            except Exception as e:
                default_log.warn("Book '%s' import failed : %s" % (bookname,e))

LoadBooks()

def BookCategoryClasses():
    return _bookcategoryclasses

def BookCategoryClass(id):
    for category in _bookcategoryclasses:
        if category.id == id:
            return category
    return None

class Default:
    id                    = 0
    title                 = u'未分类'
    description           = u''

class Tech:
    id                    = 1
    title                 = u'科技'
    description           = u''

class News:
    id                    = 2
    title                 = u'资讯'
    description           = u''

class Magazine:
    id                    = 3
    title                 = u'杂志'
    description           = u''

def LoadBookCategors():
    _bookcategoryclasses.append(Default)
    _bookcategoryclasses.append(Tech)
    _bookcategoryclasses.append(News)
    _bookcategoryclasses.append(Magazine)

LoadBookCategors()
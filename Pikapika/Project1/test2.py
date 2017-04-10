#coding:utf-8
import wikipedia

wikipedia.set_lang('zh')
w = '哈哈'
print wikipedia.page(title=w).content

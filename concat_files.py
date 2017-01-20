#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import requests
import codecs
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

stop = stopwords.words('english')
stop.append('<p>')
stop.append('</p>')
puncs = [p for p in string.punctuation]
for punc in puncs:
  stop.append(punc)

ofile = codecs.open('50_adelaide_text.txt', 'w', 'utf-8')
ifile = codecs.open('50_adelaide_text.list', 'r', 'utf-8')
for file_name in ifile:
  print 'Append %s' % file_name
  tfile = codecs.open(file_name.rstrip(), 'r', 'utf-8')
  for line in tfile:
    line = line.replace('<p>', '')
    line = line.replace('</p>', '')
    tokens = [w for w in word_tokenize(line.lower()) if w not in stop]
    line = ' '.join(tokens)
    ofile.write(line.rstrip() + ' ')
  tfile.close()

ofile.write('\n')
ifile.close()
ofile.close()

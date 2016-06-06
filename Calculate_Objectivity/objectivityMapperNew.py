#!/usr/bin/env python

import sys, zipimport

importer = zipimport.zipimporter('textblob.mod')
textblob = importer.load_module('textblob')
from textblob import TextBlob

for line in sys.stdin:
    length = 0
    for x in line:
        length += 1
    if length > 1 :
        objectivityTruthful = TextBlob(line)
        print line+"\t"+objectivityTruthful.subjectivity
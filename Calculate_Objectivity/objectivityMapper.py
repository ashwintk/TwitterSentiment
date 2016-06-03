#!/usr/bin/env python

import sys, zipimport

importer = zipimport.zipimporter('textblob.mod')
textblob = importer.load_module('textblob')
from textblob import TextBlob

for line in sys.stdin:
    # Pre-processed tweets are of the format <DATE CREATED>,<USER HANDLE>\t<TWEET TEXT>
    # Split input string to get just tweet text
    strArrray = line.split("\t")
    if len(strArrray) == 2:
        tweetText = strArrray[1]
        objectivityTruthful = TextBlob(tweetText)
        print line+"\t"+objectivityTruthful.subjectivity
#!/usr/bin/env python

import json, sys
import zipimport
importer = zipimport.zipimporter('textblob-0.11.1.mod')
textblob = importer.load_module('textblob')

arg1 = sys.argv[1]
from textblob import TextBlob

# input comes from STDIN (standard input)
for line in sys.stdin:
        try:
            parsed_json_tweets = json.loads(line)
            tweets_text = parsed_json_tweets['text']
            tweets_text = tweets_text.replace('\n', ' ').replace('\r', '')
            objectivityTruthful = TextBlob(tweets_text)
            if arg1 in tweets_text:
                matching = arg1
                print '%s\t%s' % (matching, '1')
                print objectivityTruthful.subjectivity
        except (ValueError, KeyError, TypeError):
            print ("JSON format error")


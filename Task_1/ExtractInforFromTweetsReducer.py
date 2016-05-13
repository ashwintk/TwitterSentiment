#!/usr/bin/env python

import sys

import ManipulateTweets as manip

sys.path.append('./')

# This reducer is used to remove all the stop words

# This Reducer reads data from the mapper and only prints the following information
# 1. Date Created
# 2. User Handle
# 3. Tweet text

# A complete list of internet slang words are obtained from http://webconfs.com/stop-words.php
# These words are ignored by search engines to produce faster results
# RT - refers to re-tweet and it is a stop word too as it signifies nothing
stop_words = manip.readFileandReturnAnArray("stopwords","r",True)
stop_words.append("RT")

for line in sys.stdin:
    strArray = line.split("\t")
    return_str = ""
    for i in xrange(1,len(strArray),1):
         return_str += strArray[i] +"\t"
    return_str = return_str.lstrip().strip()
    strArray = return_str.split("\t")
    if len(strArray) == 2:
        # First part of the array is the timestamp
        timestamp = strArray[0]
        # Second part of the array is the tweet text
        tweet_text = strArray[1]
        # Remove stop words from the tweet text
        tweet_text = manip.removeItemsInTweetContainedInAList(tweet_text.strip().lstrip(), stop_words, ' ')
        print "%s\t%s" % (timestamp.strip().lstrip(),tweet_text.strip().lstrip())
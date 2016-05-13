#!/usr/bin/env python

import json, sys, re, zipimport

sys.path.append('./')

import ManipulateTweets as manip

# This mapper also performs the following operations on the tweet text.
# 1. Removes all stop-words in english
# 2. Removes all words that are not in WordNet Corpus




line = raw_input()
# Split the tweet by tab
strArray = line.split("\t")
if len(strArray) == 2:
    # First part of the array is the timestamp
    timestamp = strArray[0]
    # Second part of the array is the tweet text
    tweet_text = strArray[1]
    # Remove stop words from the tweet text
    tweet_text = manip.removeItemsInTweetContainedInAList(tweet_text.strip().lstrip(), stop_words, ' ')
    print tweet_text

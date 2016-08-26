#!/usr/bin/env python

import sys, zipimport, os

sys.path.append('./')

import ManipulateTweets as manip

readFrom = ["/Users/ashwinkumar/Desktop/clinton_sentiment",
           "/Users/ashwinkumar/Desktop/trump_sentiment",
           "/Users/ashwinkumar/Desktop/cruz_sentiment"]

writeTo = ["/Users/ashwinkumar/Desktop/clinton_final_sentiment",
           "/Users/ashwinkumar/Desktop/trump_final_sentiment",
           "/Users/ashwinkumar/Desktop/cruz_final_sentiment"]


for i in xrange(0, len(writeTo)):
    positive_dict = {}
    neutral_dict = {}
    negative_dict = {}

    with open(readFrom[i], "r") as readHandle:
        print readFrom[i]
        for line in readHandle.readlines():
            strArray = line.strip().lstrip().split(",")
            if int(strArray[1]) < 0:
                if negative_dict.has_key(strArray[0]):
                    negative_dict[strArray[0]] += 1
                else:
                    negative_dict.update({strArray[0]: 1})
            elif int(strArray[1]) == 0:
                if neutral_dict.has_key(strArray[0]):
                    neutral_dict[strArray[0]] += 1
                else:
                    neutral_dict.update({strArray[0]: 1})
            elif int(strArray[1]) > 0:
                if positive_dict.has_key(strArray[0]):
                    positive_dict[strArray[0]] += 1
                else:
                    positive_dict.update({strArray[0]: 1})
    readHandle.close()

    with open(writeTo[i], "w") as writeHandle:
        print writeTo[i]
        all_keys = set(positive_dict.keys()).union(set(neutral_dict.keys()).union(set(negative_dict.keys())))
        for keys in all_keys:
            positive_count = 0
            negative_count = 0
            neutral_count = 0
            if positive_dict.has_key(keys):
                positive_count = positive_dict[keys]
            if neutral_dict.has_key(keys):
                neutral_count = neutral_dict[keys]
            if negative_dict.has_key(keys):
                negative_count = negative_dict[keys]
            writeHandle.write(
                keys + "," + str(positive_count) + "," + str(neutral_count) + "," + str(negative_count) + "\n")
    writeHandle.close()
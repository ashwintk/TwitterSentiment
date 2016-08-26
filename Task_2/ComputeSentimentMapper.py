#!/usr/bin/env python

import sys, zipimport, os

sys.path.append('./')

import ManipulateTweets as manip

# This mapper performs the following operations on the tweet text.
# 1. Calculate pleasantness score for tweets text from DAL & WordNet
# 2. Compute features for sentiment analysis
# 3. Calculate sentiment of tweets themselves

# A complete list of internet slang words are obtained from http://webconfs.com/stop-words.php
# These words are ignored by search engines to produce faster results
# RT - refers to re-tweet and it is a stop word too as it signifies nothing
stop_words = manip.readFileandReturnAnArray("stopwords","r",True)
stop_words.append("trump")

# A complete list of Dictionary of Affect in Language (DAL)
# The following code will load the list of words and
# This list was produced by C. Whissel in the following publication
# Whissell, C., 2009. Using the revised dictionary of affect in language to quantify the
# emotional undertones of samples of natural language 1, 2. Psychological reports, 105(2), pp.509-521.
DAL = manip.readNonCSVFileandReturnADict("DAL.txt", "r", " ", 0, 1, True)

# Import NLTK library
importer = zipimport.zipimporter("nltkandyaml.mod")
yaml = importer.load_module('yaml')
nltk = importer.load_module('nltk')

from nltk.corpus.reader import WordNetCorpusReader

cwd = os.getcwd()
nltk.data.path.append(cwd)
wordnet16_dir="wordnet.zip/"
wn16_path = format(wordnet16_dir)

wn = WordNetCorpusReader(os.path.abspath("{0}/{1}".format(cwd, wn16_path)), nltk.data.find(wn16_path))

for line in sys.stdin:
    strArray = line.lstrip().strip().split("\t")
    if len(strArray) == 2:
        line = strArray[1]
        line = manip.removeItemsInTweetContainedInAList(line.strip().lstrip(), stop_words, " ")
        # Convert tweet into an array of strings
        tweet_text_array = manip.splitStringAndReturnArray(line, " ")
        # Get the pleasantness score from DAL dictionary
        pleasantnessScore = manip.getPleasantnessScoreFromDAL_List(tweet_text_array, DAL)
        # Get words which do not have pleasantness score in DAL
        wordsWithoutScore = manip.getWordsWithoutPleasantnessSocre(tweet_text_array, pleasantnessScore)
        # Variable to store recomputed score
        recomputedScore = []
        if len(wordsWithoutScore) > 1:
            # Get all the synonyms for words
            synonyms_for_words = manip.getAllSynonymsInAnArray(wordsWithoutScore, wn)
            # For each synonym identify the pleasantness score
            for word in wordsWithoutScore:
                thisKeyPleasantness = manip.getPleasantnessScoreFromDAL_List(
                    synonyms_for_words[word.lower()], DAL)
                recomputedScore.append(manip.returnHighestPleasantnessScoreFromArray(thisKeyPleasantness))
        # Compute final pleasantness score
        finalPleasantnessScore = manip.readjustScore(tweet_text_array, pleasantnessScore, recomputedScore)
        # Compute sentiment from the pleasantness score
        sentimentScore = manip.getSentimentFromPlesantnessScore(finalPleasantnessScore)
        # Compute Final Sentiment
        sentimentScore = manip.computeFinalSentiment(sentimentScore)
        # Print values
        print '%s\t%s' % (str(sentimentScore), line)
        # timeStampArr = strArray[0].strip().lstrip().split(",")
        # manip.extractDateFromTimestamp(timeStampArr[0]) + "," + str(sentimentScore) + "\n")

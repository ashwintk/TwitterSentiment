#!/usr/bin/env python
# coding: utf-8

# This mapper also performs the following operations on the tweet text.
# 1. Replaces hash tags with words
# 2. Replaces emoticons with emotions (positive, negative and neutral)
# 3. Strips all punctuations other than space, apostrophe and hyphen
# 4. Replaces Internet slang words with complete words


# 9. Removes all non-ascii characters

import sys, zipimport, re
# Import tweet manipulation library
import ManipulateTweets as manip

# Set system path to current directory
sys.path.append('./')

# Load NLTK module as a side data (distibuted cache)
importer = zipimport.zipimporter('../nltk.mod')
nltk = importer.load_module('nltk')

# A complete list of internet slang words are obtained from noslang.com
# This file is stored in CSV format and passed as a side-effect
# Following code loads all the internet slang and their actual meaning into a dictionary
# In this dictionary keys are slang words and values of these keys are actual meaning of these slang

internet_slang_dict = manip.readFileandReturnADict("../Internet_slang.csv", "rb", '|', 0, 1, True,None)

# A complete list of emoticons are obtained from wikipedia.org/wiki/List_of_emoticons
# This file is stored in TSV format and passed as a side-effect
# Following code loads all the emoticons and their emotions into a dictionary
# In this dictionary keys are the emoticons and values of these keys are emotions of these emoticons

emoticons_dict = manip.readFileandReturnADict("../Emoticons.tsv", "rb", '\t', 0, 2, False,None)
print emoticons_dict
# A list of possible word contractions in english language are identified
# Negative contractions of verbs are replaced by 'NOT'
# Anything but the negative contractions are replaced with their full form

contractions_dict = manip.readFileandReturnADict("../Contractions.csv", "rU", ',', 0, 1, True)


# line = raw_input()
# # Format of dataset after first task is DateCreated,UserHandle\tTweetText
# # Split input line by tab to get tweet text
# str_Array = line.split("\t")
# tweet_text = str(str_Array[1].strip().lstrip())
# # Replace hashtags with words
# tweet_text = manip.replaceHashTagsWithWords(tweet_text)
# # Replace all the internet slang words
# tweet_text = manip.replaceOccurrencesOfAString(tweet_text,' ',internet_slang_dict,True).lstrip().strip()
# # Replace all emoticons
# tweet_text = manip.replaceOccurrencesOfAString(tweet_text,' ', emoticons_dict,False).lstrip().strip()
# # Replace all word contractions
# tweet_text = manip.replaceOccurrencesOfAString(tweet_text,' ',contractions_dict,True).lstrip().strip()
# # Remove all non-ascii characters
# tweet_text = re.sub(r'[^\x00-\x7F]+','', tweet_text)
# # Remove all punctuations other than space, apostrophe and hyphen
# tweet_text = re.sub(r'[^a-z|A-Z|0-9|\'|\s|-]*',' ', tweet_text)
# # Convert multiple white spaces into a single white space
# tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)

# # convert tweet text into tokens using nltk package
# tokens = nltk.word_tokenize(tweet_text.strip().lstrip())
#
# print tokens

# # Remove internet slang terms
# non_slang = []
# for t in tokens:
#     if internet_slang_dict.has_key(t.lower()):
#         non_slang_word = internet_slang_dict[t.lower()]
#         # Remove all punctuations other than space, apostrophe and hyphen
#         non_slang_word = re.sub(r'[^a-z|A-Z|0-9|\'|\s|-]*', ' ', non_slang_word)
#         non_slang_word = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(non_slang_word)
#         non_slang.append(non_slang_word)
#     else:
#         non_slang.append(t)
# modified_tweet = ' '.join(non_slang)
# print modified_tweet

sys.stderr.write('CHK Pt 10')
# Replace all emoticons
tweet_text = manip.replaceOccurrencesOfAString(tweet_text, ' ', emoticons_dict, False).lstrip().strip()
sys.stderr.write('CHK Pt 11')
sys.stderr.write('CHK Pt 12')
# Remove all non-ascii characters
tweet_text = re.sub(r'[^\x00-\x7F]+', '', tweet_text)
sys.stderr.write('CHK Pt 13')
# Remove all punctuations other than space, apostrophe and hyphen
tweet_text = re.sub(r'[^a-z|A-Z|0-9|\'|\s|-]*', ' ', tweet_text)
sys.stderr.write('CHK Pt 14')
# Convert multiple white spaces into a single white space
tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
sys.stderr.write('CHK Pt 15')
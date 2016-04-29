#!/usr/bin/env python
import re

# This function is used to remove all the URL's in a tweet
def removeURL(tweetText):
    return re.sub('((www\.[^\s]+)|(https?://[^\s]+))','',tweetText)

# This function is used to remove user mentions in a tweet
def removeUserMentions(tweetText):
    return re.sub('@[^\s]+','',tweetText)

# This function is used to convert multiple white spaces into a single white space
def convertMultipleWhiteSpacesToSingleWhiteSpace(tweetText):
    return re.sub('[\s]+', ' ', tweetText)

# Function used to strip non-alpha numeric characters in a tweet
def stripNonAlphaNumeric(text):
    pattern = re.compile('[^a-zA-Z0-9 ]')
    return re.sub(r'\s\s','',re.sub(pattern,' ',text))

# This function replaces any hash tag in a tweet with the word
def replaceHashTagsWithWords (tweetText):
    return re.sub(r'#([^\s]+)', r'\1', tweetText)

# This function is used to chack if a word occurs in a tweet
def isWordInTweet(tweetText,FilterWord):
    if FilterWord.lower() in tweetText.lower():
        return True
    else:
        return False

# This function removes new line & return carriages from tweets
def stripNewLineAndReturnCarriage(tweetText):
    return tweetText.replace('\n', ' ').replace('\r', '').strip().lstrip()

# This function replaces words with repeating 'n' or more same characters with a single character
def replaceRepeatedCharacters(tweetText):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1\1", tweetText)

# Filter tweets other than passed language
def CheckLanguage(tweetLanguage,langFilter):
    #Check for Rule 1 - Tweet words are in Group1 only
    if tweetLanguage.strip().lstrip().lower()==langFilter.strip().lstrip().lower():
        return True
    else:
        return False
# This function removes punctuations from tweet text
def stripTweet(tweetText):
    tweetText=tweetText.strip('\'"')
    return tweetText.strip('\'"?,.')
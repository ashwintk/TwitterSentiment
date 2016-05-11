#!/usr/bin/env python
import re, csv, sys

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
    if tweetLanguage.strip().lstrip().lower()==langFilter.strip().lstrip().lower():
        return True
    else:
        return False

# This function removes punctuations from tweet text
def stripTweet(tweetText):
    tweetText=tweetText.strip('"-')
    return tweetText.strip('"?,.')

# This function is used to convert multiple white spaces into a single white space
def convertMultipleWhiteSpacesToSingleWhiteSpace(tweetText):
    return re.sub('[\s]+', ' ', tweetText)

# This function can be used to parse a file given a delimiter, file name and key & value to select
def readFileandReturnADict(fileName, readMode, delimiter, keyIndex, valueIndex, isLower, fileDialect = None):
    mydict={}
    with open(fileName, readMode) as readHandle:
        if fileDialect is None:
            fileDialect = csv.Sniffer().sniff(readHandle.read(), delimiters=delimiter)
        readHandle.seek(0)
        reader = csv.reader(readHandle, fileDialect)
        for line in reader:
            if isLower:
                mydict.update({line[keyIndex].lower(): line[valueIndex]})
            else:
                mydict.update({line[keyIndex]: line[valueIndex]})
    readHandle.close()
    return mydict

# This function splits a string by a character and replaces words from key of the dictionary
def replaceOccurrencesOfAString(text,splitBy,dict,lowerFlag):
    str_array=text.split(splitBy)
    return_str=""
    for word in str_array:
        key_to_Search=str(word).strip().lstrip()
        if len(key_to_Search) >1:
            if lowerFlag:
                key_to_Search=word.lower()
            if dict.has_key(key_to_Search):
                return_str+=" "+dict[key_to_Search]
            else:
                return_str += " " + word
    return return_str


# This function can be used to replace emoticons with their emotions (POSITIVE/NEGATIVE/NEUTRAL)
# A complete list of emoticons are obtained from wikipedia.org/wiki/List_of_emoticons
def replaceEmoticons(tweet_texts, splitBy,lowerFlag):
    str_array = tweet_texts.split(splitBy)
    return_str = ""
    for word in str_array:
        wordToFind = str(word).strip().lstrip()
        if lowerFlag:
            wordToFind = word.lower()
        if (wordToFind == ":-)" or wordToFind == ":)" or wordToFind == ":D" or wordToFind == ":o)" or wordToFind == ":]" or wordToFind == ":3" or
                    wordToFind == ":c)" or wordToFind == ":>" or wordToFind == "=]" or wordToFind == "8)" or wordToFind == "=)" or
                    wordToFind == ":}" or wordToFind == ":^)" or wordToFind == ":-D" or wordToFind == "8-D" or wordToFind == "8D" or
                    wordToFind == "x-D" or wordToFind == "xD" or wordToFind == "X-D" or wordToFind == "XD" or wordToFind == "=-D" or
                    wordToFind == "=D" or wordToFind == "=-3" or wordToFind == "=3" or wordToFind == "B^D" or wordToFind == ":-))" or
                    wordToFind == ":'-)" or wordToFind == ":')" or wordToFind == ":*" or wordToFind == ":-*" or wordToFind == ":^*" or
                    wordToFind == "( '}{' )" or wordToFind == ";-)" or wordToFind == ";)" or wordToFind == "*-)" or wordToFind == "*)" or
                    wordToFind == ";-]" or wordToFind == ";]" or wordToFind == ";D" or wordToFind == ";^)" or wordToFind == ":-," or
                    wordToFind == ">:P" or wordToFind == ":-P" or wordToFind == ":P" or wordToFind == "X-P" or wordToFind == "x-p" or
                    wordToFind == "xp" or wordToFind == "XP" or wordToFind == ":-p" or wordToFind == ":p" or wordToFind == "=p" or
                    wordToFind == ":-p" or wordToFind == ":p" or wordToFind == ":p" or wordToFind == ":-p" or wordToFind == ":-b" or
                    wordToFind == ":b" or wordToFind == "d:" or wordToFind == "O:-)" or wordToFind == "0:-3" or wordToFind == "0:3" or
                    wordToFind == "0:-)" or wordToFind == "0:)" or wordToFind == "0;^)" or wordToFind == "o/\o" or wordToFind == "^5" or
                    wordToFind == ">_>^" or wordToFind == "^<_<" or wordToFind == "[;-)" or wordToFind == "#-)" or wordToFind == "\o/" or
                    wordToFind == "*\0/*" or wordToFind == "<3"):
            return_str += " POSITIVE"
        elif (wordToFind == ">:[" or wordToFind == ":-(" or wordToFind == ":(" or wordToFind == ":-c" or wordToFind == ":c" or
                      wordToFind == ":-<" or wordToFind == ":<" or wordToFind == ":-[" or wordToFind == ":[" or
                      wordToFind == ":{" or wordToFind == ":-||" or wordToFind == ":@" or wordToFind == ">:(" or
                      wordToFind == ":'-(" or wordToFind == ":'(" or wordToFind == "D:<" or wordToFind == "D:" or
                      wordToFind == "D8" or wordToFind == "D;" or wordToFind == "D=" or wordToFind == "DX" or
                      wordToFind == "v.v" or wordToFind == "D-':" or wordToFind == ">:\\" or wordToFind == ">:/" or
                      wordToFind == ":-/" or wordToFind == ":-." or wordToFind == ":/" or wordToFind == ":\\" or
                      wordToFind == "=/" or wordToFind == "=\\" or wordToFind == ":L" or wordToFind == "=L" or
                      wordToFind == ":S" or wordToFind == ">.<" or wordToFind == ":$" or wordToFind == ">:)" or
                      wordToFind == ">;)" or wordToFind == ">:-)" or wordToFind == "}:-)" or wordToFind == "}:)" or
                      wordToFind == "3:-)" or wordToFind == "3:)" or wordToFind == "|-O" or wordToFind == ":-&" or
                      wordToFind == ":&" or wordToFind == "%)" or wordToFind == ":-###.." or wordToFind == ":###.." or
                      wordToFind == "<:-<" or wordToFind == "<*)))-{" or wordToFind == "><(((*>" or wordToFind == "><>" or wordToFind == "</3"):
            return_str += " NEGATIVE"
        elif (wordToFind == ";{" or wordToFind == ">:O" or wordToFind == ":-O" or wordToFind == ":O" or wordToFind == ":-o" or
                      wordToFind == ":o" or wordToFind == "8-0" or wordToFind == "O_O" or wordToFind == "o-o" or wordToFind == "O_o" or
                      wordToFind == "o_O" or wordToFind == "o_o" or wordToFind == "O-O" or wordToFind == ":|" or wordToFind == ":-|" or
                      wordToFind == ":-X" or wordToFind == ":X" or wordToFind == ":-#" or wordToFind == ":#" or wordToFind == ":-J" or
                      wordToFind == "%-)"):
            return_str += " NEUTRAL"
        else:
            return_str += " " + wordToFind
    return return_str
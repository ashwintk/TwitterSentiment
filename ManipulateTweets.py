#!/usr/bin/env python
import re, csv, sys

# This function is used to split a string and return an array based on a passed delimiter
def splitStringAndReturnArray(text, delimiter):
    return text.lstrip().strip().split(delimiter)
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
    return re.sub(r"(.)\1{3,}",r"\1", tweetText)

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
# A complete list of emoticons are obtained from www.wikipedia.org/wiki/List_of_emoticons
def replaceEmoticons(tweet_texts, splitBy,lowerFlag):
    str_array = splitStringAndReturnArray(tweet_texts, splitBy)
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

# This function will return the candidate names if they are in a contained in a tweet
def identifyCandidates(tweet_text,candidate_dict):
    keys_to_check = candidate_dict.keys()
    matching = [s for s in keys_to_check if s in tweet_text.lower()]
    candidates = set()
    if len(matching) > 0:
        for item in matching:
            candidates.add(candidate_dict[item])
    else:
        candidates.add('other')
    return list(candidates)

# This function removes items from a list in a tweet text
def removeItemsInTweetContainedInAList(tweet_text,stop_words,splitBy):
    wordsArray = splitStringAndReturnArray(tweet_text,splitBy)
    StopWords = list(set(wordsArray).intersection(set(stop_words)))
    return_str=""
    for word in wordsArray:
        if word not in StopWords:
            return_str += word + splitBy
    return return_str.strip().lstrip()

# This function reads a file and returns its contents as an array
def readFileandReturnAnArray(fileName, readMode, isLower):
    myArray=[]
    with open(fileName, readMode) as readHandle:
        for line in readHandle.readlines():
            lineRead = line
            if isLower:
                lineRead = lineRead.lower()
            myArray.append(lineRead.strip().lstrip())
    readHandle.close()
    return myArray

# This function will read a non CSV/TSV file and load the contents into a dictionary
def readNonCSVFileandReturnADict(fileName, readMode, delimiter, keyIndex, valueIndex, isLower):
    mydict={}
    with open(fileName, readMode) as readHandle:
        for line in readHandle.readlines():
            line = convertMultipleWhiteSpacesToSingleWhiteSpace(line)
            line = splitStringAndReturnArray(line, delimiter)
            if isLower:
                mydict.update({line[keyIndex].lower(): line[valueIndex]})
            else:
                mydict.update({line[keyIndex]: line[valueIndex]})
    readHandle.close()
    return mydict

# This function will return the pleasantness score for a given tweet text
def getPleasantnessScoreFromDAL_List (tweet_text_array, dict):
    pleasantnessScore =[]
    for word in tweet_text_array:
        if dict.has_key(word.lower()):
            pleasantnessScore.append(dict[word.lower()])
        else:
            pleasantnessScore.append("-")
    return pleasantnessScore

# This function will return the words whose pleasantness score hasn't been calculated
def getWordsWithoutPleasantnessSocre(tweet_text_array, scores):
    wordsWithoutScore =[]
    for i in xrange(0,len(scores)):
        if scores[i] == '-':
            wordsWithoutScore.append(tweet_text_array[i])
    return wordsWithoutScore

# This function will get all synonyms for all the words in a given array
# This function returns a dictionary with key as the word and synonyms as array of values
def getAllSynonymsInAnArray(word_array, wn):
    dict = {}
    for word in word_array:
        synonyms = []
        for syn in wn.synsets(word):
            for synon in syn.lemma_names():
                synonyms.append(str(synon).lower().replace("_"," "))
        dict.update({word.lower():synonyms})
    return dict

# This function will go through a pleasantness score array and return the maximum value
# If no value is found, or the array is empty it will return a zero
def returnHighestPleasantnessScoreFromArray(scoreArray):
    retscore = 0
    if len(scoreArray) <=0:
        return 0
    else:
        for score in scoreArray:
            if score != '-' and score > retscore:
                retscore = score
        return retscore

# This function computes adjusted score. It takes pleasantness score from DAL list, original tweet
# pleasantness score computed from synonyms in WordNet as arguments and returns a dictionary
# Key for this dictionary is the word with a valid score and value is the pleasantness score of the word
# or the highest pleasantness score of a synonym of the word
# Words & synonyms of words which are not in either DAL are ignored
def readjustScore(tweet_array, originalPleasantnessScore, synonymsPleasantnessScore):

    dict = {}
    second_counter = 0
    for i in xrange(0,len(tweet_array)):
        if originalPleasantnessScore[i] != '-':
            dict.update({tweet_array[i]:originalPleasantnessScore[i]})
        else:
            if len(synonymsPleasantnessScore) >0 :
                if synonymsPleasantnessScore[second_counter] != 0:
                    dict.update({tweet_array[i]: synonymsPleasantnessScore[second_counter]})
                second_counter += 1
    return dict

# This method accepts a dictionary and returns a sentiment score attached to it
def getSentimentFromPlesantnessScore(pleasantnessScore):
    sentimentScore = []
    for key in pleasantnessScore:
        curentScore = float(pleasantnessScore[key])
        curentScore /= 3
        if curentScore < 0.5:
            sentimentScore.append(-1)
        elif curentScore > 0.8:
            sentimentScore.append(1)
        else:
            sentimentScore.append(0)
    return sentimentScore

# This method will return the final sentiment score from an array of sentiment scores
def computeFinalSentiment(sentimentArray):
    ret_sentiment =0
    for item in sentimentArray:
        ret_sentiment += int(item)
    return ret_sentiment

# Extract date from timestamp
def extractDateFromTimestamp(timestamp):
    from dateutil import parser
    d = parser.parse(timestamp.strip().lstrip())
    return str(d.date())
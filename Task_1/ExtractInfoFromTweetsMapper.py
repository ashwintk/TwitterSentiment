#!/usr/bin/env python

import json, sys, re

sys.path.append('./')

import ManipulateTweets as manip

# This mapper performs the following operations on the tweet text.
# 1. Remove URL's and user mentions.
# 2. Replaces new line character (\n) with space and return carriage character (\r) with ''
# 4. Replaces hash tags with words
# 5. Replaces emoticons with emotions (positive, negative and neutral)
# 6. Strips all punctuations other than space, apostrophe and hyphen
# 7. Replaces Internet slang words with complete words
# 8. Replaces multiple white spaces with a single space
# 9. Identifies which candidate the tweet is about
# 10. Removes stop words from tweets
# 11. Removes double quotes from string


# This mapper extracts only the following information from tweets
# 1. Date Created
# 2. User Handle
# 3. Tweet text
# 4. Candidate

# A complete list of internet slang words are obtained from noslang.com
# This file is stored in CSV format and passed as a side-effect
# Following code loads all the internet slang and their actual meaning into a dictionary
# In this dictionary keys are slang words and values of these keys are actual meaning of these slang

internet_slang_dict = manip.readFileandReturnADict("internet_slang.csv", "rb", '|', 0, 1, True,None)

# A list of possible word contractions in english language are identified
# Negative contractions of verbs are replaced by 'NOT'
# Anything but the negative contractions are replaced with their full form

contractions_dict = manip.readFileandReturnADict("Contractions.csv", "rU", ',', 0, 1, True)

# A list of candidate names and their campaign chants and slogans are saved as a CSV file.
# This information is loaded into a dictionary
candidates_dict = manip.readFileandReturnADict("Candidates.csv","r",",",0,1, True, None)

# A complete list of internet slang words are obtained from http://webconfs.com/stop-words.php
# These words are ignored by search engines to produce faster results
# RT - refers to re-tweet and it is a stop word too as it signifies nothing
stop_words = manip.readFileandReturnAnArray("stopwords","r",True)
stop_words.append("RT")
stop_words.append("&amp;")
stop_words.append("&amp")


for line in sys.stdin:
    try:
        # Load Tweets
        parsed_json_tweets = json.loads(line)
        # Extract date created
        date_created = parsed_json_tweets['created_at'].lstrip().strip()
        # Extract user handle
        user_handle = parsed_json_tweets['user']['screen_name'].lstrip().strip()
        # Extract tweet text
        tweet_text = parsed_json_tweets['text'].lstrip().strip()
        if len(tweet_text) > 1:
            # Remove new line and carriage return
            tweet_text = manip.stripNewLineAndReturnCarriage(tweet_text)
            # Remove URL's & User Mentions
            tweet_text = manip.removeURL(tweet_text)
            tweet_text = manip.removeUserMentions(tweet_text)
            # Replace sequence of repeated characters by three characters
            tweet_text = manip.replaceRepeatedCharacters(tweet_text)
            # Convert multiple white spaces to a single white space
            tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
            # Replace hashtags with words
            tweet_text = manip.replaceHashTagsWithWords(tweet_text)
            # Replace all the internet slang words
            tweet_text = manip.replaceOccurrencesOfAString(tweet_text, ' ', internet_slang_dict, True).lstrip().strip()
            # Replace all word contractions
            tweet_text = manip.replaceOccurrencesOfAString(tweet_text, ' ', contractions_dict, True).lstrip().strip()
            # Replace all emoticons
            tweet_text = manip.replaceEmoticons(str(tweet_text), ' ', False).lstrip().strip()
            # Convert multiple white spaces to a single white space
            tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
            # Get candidates in the tweets
            candidates = manip.identifyCandidates(tweet_text,candidates_dict)
            # Remove double quotes
            tweet_text = re.sub(r"\"", r"", tweet_text)
            # Remove stop words from tweets
            tweet_text = manip.removeItemsInTweetContainedInAList(tweet_text.strip().lstrip(),stop_words," ")
            # Print the tweet with the candidate it talks about
            for candidate in candidates:
                # Send Date created, user handle and tweet text as output
                print '%s\t%s,%s\t%s' % (candidate,date_created, user_handle, tweet_text)
    except ValueError:
        continue

#!/usr/bin/env python

import json, sys

sys.path.append('./')

import ManipulateTweets as manip
#This mapper reads the twitter data and extracts only the following information
# 1. Data Created
# 2. User Handle
# 3. Tweet text

# This mapper also performs the following operations on the tweet text.
# 1. Remove URL's and user mentions.
# 2. Replaces new line character (\n) with space and return carriage character (\r) with ''

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
        # Remove new line and carriage return
        tweet_text = manip.stripNewLineAndReturnCarriage(tweet_text)
        # Remove URL's & User Mentions
        tweet_text = manip.removeURL(tweet_text)
        tweet_text = manip.removeUserMentions(tweet_text)
        # Replace sequence of repeated characters by three characters
        tweet_text=manip.replaceRepeatedCharacters(tweet_text)
        # Convert multiple white spaces to a single white space
        tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
        # Send Date created, user handle and tweet text as output
        print '%s,%s\t%s' %(date_created,user_handle,tweet_text)
    except(ValueError):
        print ("JSON format error")
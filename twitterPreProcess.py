#!/usr/bin/env python

import json, sys, re

sys.path.append('./')

import ManipulateTweets as manip

# 5. Replaces emoticons with emotions (positive, negative and neutral)
# 6. Strips all punctuations other than space, apostrophe and hyphen
# 7. Replaces Internet slang words with complete words
# 8. Replaces multiple white spaces with a single space
# 9. Identifies which candidate the tweet is about

# 11. Removes double quotes from string


# A complete list of internet slang words are obtained from noslang.com
# This file is stored in CSV format and passed as a side-effect
# Following code loads all the internet slang and their actual meaning into a dictionary
# In this dictionary keys are slang words and values of these keys are actual meaning of these slang

internet_slang_dict = manip.readFileandReturnADict("internet_slang.csv", "rb", '|', 0, 1, True,None)

# A list of possible word contractions in english language are identified
# Negative contractions of verbs are replaced by 'NOT'
# Anything but the negative contractions are replaced with their full form

contractions_dict = manip.readFileandReturnADict("Contractions.csv", "rU", ',', 0, 1, True)



for line in sys.stdin:
    try:
        # Load Tweets
        parsed_json_tweets = json.loads(line)
        # Extract tweet text
        tweet_text = parsed_json_tweets['text'].lstrip().strip()
        length = 0
        for x in tweet_text:
            length += 1
        if length > 1:
            # Convert multiple white spaces to a single white space
            tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
            # Replace all the internet slang words
            tweet_text = manip.replaceOccurrencesOfAString(tweet_text, ' ', internet_slang_dict, True).lstrip().strip()
            # Replace all word contractions
            tweet_text = manip.replaceOccurrencesOfAString(tweet_text, ' ', contractions_dict, True).lstrip().strip()
            # Replace all emoticons
            tweet_text = manip.replaceEmoticons(str(tweet_text), ' ', False).lstrip().strip()
            # Convert multiple white spaces to a single white space
            tweet_text = manip.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
            # Remove double quotes
            tweet_text = re.sub(r"\"", r"", tweet_text)
            print '%s' % (tweet_text)
    except ValueError:
        continue

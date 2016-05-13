#!/usr/bin/env python

import json, sys, re

sys.path.append('./')

import ManipulateTweets as manip

# A list of candidate names and their campaign chants and slogans are saved as a CSV file.
# This information is loaded into a dictionary
candidates_dict = manip.readFileandReturnADict("../Candidates.csv","r",",",0,1, True, None)

line = raw_input()
print manip.identifyCandidates(line,candidates_dict)

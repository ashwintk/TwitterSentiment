#!/usr/bin/env python

import sys

sys.path.append('./')


# This Reducer reads output data and prints only the following information
# 1. Date Created
# 2. User Handle
# 3. Tweet text

for line in sys.stdin:
    strArray = line.split("\t")
    return_str = ""
    for i in xrange(1,len(strArray),1):
         return_str += strArray[i] +"\t"
    print "%s" % (return_str.strip().lstrip())
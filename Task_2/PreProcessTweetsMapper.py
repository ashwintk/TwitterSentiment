# #!/usr/bin/env python
#
import json, sys, re, zipimport
#
# sys.path.append('./')
#
# import ManipulateTweets as manip





line = raw_input()
print re.sub(r"\"", r"", line)

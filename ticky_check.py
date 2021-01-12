#!/usr/bin/env python3

import os
import sys
import re
import operator
import csv

# Dict: Count number of entries for each user
per_user_info = {}  # Splitting between INFO and ERROR
per_user_error = {}  # Splitting between INFO and ERROR

# Dict: Number of different error messages
errors = {}

# Sample Error
# "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"

with open('small.log') as file:
    # read each line
    for line in file.readlines():
        # regex search
        info = re.search(r'INFO: ([\w].*)', line)
        user = re.search(r'\(.*?\)', line)
        error = re.search(r'ERROR: ([\w].*)', line)

        # Checks for successful match
        if info is not None:
            i = info.group(0)
            u = user.group(0)
            if not u in per_user_info:
                per_user_info[u] = 1
            else:
                per_user_info[u] += 1

        # Checks for ERROR match
        if error is not None:
            e = error.group(0)
            u = user.group(0)
            if not u in per_user_error:
                per_user_error[u] = 1
            else:
                per_user_error[u] += 1

        # Checks if error got a match
        if error is not None:
            e = error.group(0)
            if not e in errors:
                errors[e] = 1
            else:
                errors[e] += 1
file.close()


# Sorted by VALUE (Most common to least common)
print('ERRORS:', sorted(errors.items(),
                        key=operator.itemgetter(1), reverse=True))

# Sorted by USERNAME
print('Per User INFO:', sorted(per_user_info.items(), key=operator.itemgetter(0)))
print('Per User ERROR:', sorted(per_user_error.items(), key=operator.itemgetter(0)))

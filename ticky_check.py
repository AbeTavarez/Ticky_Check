#!/usr/bin/env python3

import os
import sys
import re
import operator
import csv

# Dict: Number of different error messages
errors = {}
# Dict: Count number of entries for each user
per_user = {}  # Splitting between INFO and ERROR

# Sample Error
# "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"

with open('small.log') as file:
    # read each line
    for line in file.readlines():
        # regex search
        info = re.search(r'INFO: ([\w].*)', line)
        error = re.search(r'ERROR: ([\w].*)', line)

        # Checks for successful match
        if info is not None:
            e = info.group(0)
            print(e)
            if not e in per_user:
                per_user[e] = 1
            else:
                per_user[e] += 1

        # Checks if error got a match
        if error is not None:
            e = error.group(0)
            if not e in errors:
                errors[e] = 1
            else:
                errors[e] += 1
file.close()

print('Erros Dict', errors)
print('Per User Dict', per_user)

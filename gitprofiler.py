#!/usr/bin/env python3

"""
gitprofiler.py

Author: Dr. Andreas Janzen, janzen@gmx.net
Date: 2020-07-15
"""

import os
import sys

from github import Github


gh = Github()
print("Jetzt habe ich irgendwelchen Quatsch eingefügt.")

user = gh.get_user("aojanzen")
print("This is a test.")

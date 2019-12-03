#!/usr/bin/python3

import os, time

print("This is a test code for Python3")

print("Hello %s, let us be friends!" % os.environ["USER"])

print("Today is %s" % time.strftime("%c"))

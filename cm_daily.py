#!/usr/bin/python

import json
import re
from subprocess import Popen, PIPE

with open('projects.txt', 'r') as f:
    cm_p = [p.strip() for p in f.readlines()]
    f.closed

# print cm_p

merged = Popen(["ssh", "-p", "29418", "r.cyanogenmod.com", "gerrit", "query",
    "status:merged", "limit:5", "age:1d", "--format=JSON"],
    stdout=PIPE).communicate()[0]

for c in merged.strip().split("\n"):
    change = json.loads(c)

    if change['project'] in cm_p:
        print change['url'],
        print change['project'],
        print change['subject'],
        print change['branch']

    # for p in cm_p:
        # if re.search('(?<=-)\w+', 'spam-egg'):
    print "'%s'" % change

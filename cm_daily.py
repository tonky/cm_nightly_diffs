#!/usr/bin/python

import json
import re
from subprocess import Popen, PIPE
import time

last_run = time.time() - 60*60*24

with open('projects.txt', 'r') as f:
    cm_p = [p.strip() for p in f.readlines()]
    f.closed

merged = Popen(["ssh", "-p", "29418", "r.cyanogenmod.com", "gerrit", "query",
    "status:merged", "limit:80", "--format=JSON"],
    stdout=PIPE).communicate()[0]

print "[LIST]"

for c in merged.strip().split("\n"):
    change = json.loads(c)

    if 'lastUpdated' in change and change['lastUpdated'] < last_run:
        continue

    if 'project' in change and change['project'] in cm_p:
        print "[*][URL=\"%s\"]%s[/URL] (%s)" % (change['url'], change['subject'],
                change["project"].split("/")[1])
        # print time.ctime(change['lastUpdated'])
        # print change['branch']
        # print change['url']
        # print "%s: %s" % (time.ctime(change['lastUpdated']), change['url'])

print "[LIST/]"

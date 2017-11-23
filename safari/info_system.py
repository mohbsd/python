#!/usr/bin/env python
# A simple system information script

import subprocess

# command 1 uname
uname = "uname"
uname_arg = "-a"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])

# command 2 df
diskspace = "df"
diskspace_arg = "-h"
print "Gathering diskspace infomation with %s command:\n " % diskspace_arg
subprocess.call([diskspace, diskspace_arg])

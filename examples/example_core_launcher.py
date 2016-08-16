#!/usr/bin/env python

import pylauncher

##
## Emulate the classic launcher, using a one liner
##

pylauncher.ClassicLauncher("commandlines",
                           debug="job+task+host+exec+command",
                           cores=2)

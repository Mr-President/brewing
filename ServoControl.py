#! /usr/bin/env python 

import servoblaster
import time
servoblaster.initialize([29],100000,0)
servoblaster.position(0, 120)
time.sleep(2)
servoblaster.position(0,220)
time.sleep(2)
servoblaster.stop()

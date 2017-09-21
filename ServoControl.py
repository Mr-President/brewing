#! /usr/bin/env python 

import servoblaster
import time
servoblaster.initialize([29],100000,0)
servoblaster.position(0, 500)
time.sleep(2)
servoblaster.position(0,1000)
time.sleep(2)
servotblaster.stop()

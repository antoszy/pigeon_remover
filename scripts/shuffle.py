#!/usr/bin/env python

import glob
import sys
import os
import random

if __name__ == "__main__":
    if len(sys.argv)<2:
        filelist = glob.glob("./*.jpg")
    else:
        filelist = glob.glob(sys.argv[1]+ "/*.jpg")
    
    filelist = random.shuffle(b)

    print(filelist)

    for f in filelist:
        print(f) 

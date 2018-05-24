#!/usr/bin/env python
import glob
import sys
import os
import random

if __name__ == "__main__":

    if len(sys.argv)>1:
        os.chdir(sys.argv[1])
    
    filelist = glob.glob("*.jpg")
   
    random.shuffle(filelist)
    number = 0

    for f in filelist:
        os.rename( f, str(number).zfill(5) + ".jpg")
        number = number + 1

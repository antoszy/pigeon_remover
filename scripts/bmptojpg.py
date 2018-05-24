#!/usr/bin/env python

import glob
import sys
import cv2
import os

if __name__ == "__main__":
    if len(sys.argv)<2:
        filelist = glob.glob("./*.bmp")
    else:
        filelist = glob.glob(sys.argv[1]+ "/*.bmp")

    for f in filelist:
        img = cv2.imread( f, cv2.IMREAD_COLOR )
        cv2.imwrite( f[:f.rfind(".")] + ".jpg", img)
        os.remove(f)
        

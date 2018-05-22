#!/usr/bin/env python3

import glob
import sys
import cv2

if __name__ == "__main__":
	print(sys.argv);
	if len(sys.argv)<2:
		filelist = glob.glob("./*")
	else:
		filelist = glob.glob(sys.argv[1])

	for f in filelist:
		print(f)
	print(cv2.__version__)

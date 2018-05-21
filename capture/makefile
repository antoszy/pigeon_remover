all: capture

capture: capture.o
	gcc -o capture capture.o -lstdc++ -lopencv_core -lopencv_highgui -lopencv_videoio -lopencv_imgproc -lopencv_imgcodecs

capture.o: capture.cpp
	gcc -c -std=c++11 capture.cpp



clean:
	rm capture.o capture 


install:
	cp capture /usr/local/bin

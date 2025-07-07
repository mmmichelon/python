import atexit
from time import clock
import math
import functools

def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % \
        functools.reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])

line = "="*40
def log(s, elapsed=None):
    print(line)
    print(secondsToStr(clock()), '-', s)
    if elapsed:
        print("Elapsed time:", elapsed)
    print(line)
    print(" ")

def endlog():
    end = clock()
    elapsed = end-start
    log("End Program", secondsToStr(elapsed))

def now():
    return secondsToStr(clock())

start = clock()
atexit.register(endlog)
log("Start Program")
i = 0
while( i < 100):
    i = i + 1
    print(i)
    
# got from Nicojo @ stackoverflow | code: 1557571
# adjusted as reduce function doesn't work on python 3000 anymore

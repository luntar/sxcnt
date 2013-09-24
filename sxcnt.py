#!/usr/bin/env python

import sys
import struct

print "sysex counter v1.0"
f0cnt = 0
f7cnt = 0

for arg in sys.argv:
    fname = arg
#    print arg
if fname == sys.argv[0]:
    exit

#print 'Input: ' + fname
f = open(fname,'rb')
try:
    byte = f.read(1)
    while byte != "":
        b = struct.unpack('B',byte)[0]
        #print b
        if b == 240:
            f0cnt = f0cnt + 1
        elif b == 247:
            f7cnt = f7cnt + 1

        byte = f.read(1)
finally:
    f.close()

print str(min(f0cnt,f7cnt))



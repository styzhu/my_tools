'''
add /" at the beginning and //n/" at the end of each line
take argument as the source file
Created on Jan 4, 2015

@author: FunghiApe
'''

import sys

print "File location: ", sys.argv[1]

with open(sys.argv[1], "r") as f:
    lineList = f.readlines()
    
    maxLineLength = 0
    for l in lineList:
        l = l.rstrip('\n')
        if len(l) > maxLineLength:
            maxLineLength = len(l)
    
    extraSpaceLength = 0
    for l in lineList:
        l = l.rstrip('\n')
        extraSpaceLength = maxLineLength - len(l) + 4
        extraSpace = " " * extraSpaceLength
        print "\"{0}{1}\\n\"".format(l, extraSpace)
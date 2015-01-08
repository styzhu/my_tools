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
    newList = []
    maxLineLength = 0
    for l in lineList:
        l = l.rstrip('\n')
        l = l.replace('\t', '    ')
        newList.append(l)
        if len(l) > maxLineLength:
            maxLineLength = len(l)
    
    extraSpaceLength = 0
    for nl in newList:
        nl = nl.rstrip('\n')
        extraSpaceLength = maxLineLength - len(nl) + 4
        extraSpace = " " * extraSpaceLength
        print "\"{0}{1}\\n\"".format(nl, extraSpace)
#!/usr/bin/env python

"""
compress feature ids to a continuous list [1-n]
"""

import sys
import csv

input_file  = sys.argv[1]
output_file = sys.argv[2]

try:
    skip_headers = sys.argv[4]
except IndexError:
    skip_headers = 0


output = open( output_file, 'w' )

reader = csv.reader( open( input_file, 'rb' ) )

if skip_headers:
    headers = reader.next()
    print 'skipping', headers

idict = {}
hdict = {}

for line in reader:
    # print 'line', line
    h = line[0]
    i = line[1]
    
    if not idict.has_key(h):
        hdict[h] = len(hdict)+1
    
    if not idict.has_key(i):
        idict[i] = len(idict)+1

    new_line = "%s,%s\n" % ( hdict[h], idict[i] )
    output.write( new_line )

# print idict

index = csv.writer(open(output_file + ".id0", "w"))
for key, val in hdict.items():
    index.writerow([key, val])
    
index = csv.writer(open(output_file + ".id1", "w"))
for key, val in idict.items():
    index.writerow([key, val])


#!/usr/bin/env python

"""
compress feature ids to a continuous list [1-n]
"""

import sys
import csv

input_file  = sys.argv[1]
output_file = sys.argv[2]
index_file  = sys.argv[3]


output = open( output_file, 'w' )

reader = csv.reader( open( input_file ), delimiter = " " )

idict = {}

for line in reader:
    label = line.pop( 0 )
    if line[-1].strip() == '':
        line.pop( -1 )

    #print line

    line = map( lambda x: tuple( x.split( ":" )), line )
    #print line
    # ('1', '0.194035105364'), ('2', '0.186042408882'), ('3', '-0.148706067206'), ...

    new_line = [label] #label

    for i, v in line:
        if not idict.has_key(i):
            idict[i] = len(idict)+1

        new_line.append( "%s:%s" % ( idict.get(i), v ) )

    new_line = " ".join( new_line ) + "\n"
    output.write( new_line )

print idict
    
index = csv.writer(open(index_file, "w"))
for key, val in idict.items():
    index.writerow([key, val])


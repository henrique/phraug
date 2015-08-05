#!/usr/bin/env python

"""
generates data in a n-fold manner
"""

import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]


reader = csv.reader( open( input_file ), delimiter = " " )

for line in reader:
    label = line.pop( 0 )
    if line[-1].strip() == '':
        line.pop( -1 )

    #print line

    line = map( lambda x: tuple( x.split( ":" )), line )
    #print line
    # ('1', '0.194035105364'), ('2', '0.186042408882'), ('3', '-0.148706067206'), ...

    for i, v in line:
        new_line = [i] #label
        for i2, v2 in line:
            if i2 != i:
                new_line.append( "%s:%s" % ( i2, v2 ) )

        new_line = " ".join( new_line ) + "\n"
        o = open( output_file, 'a' )
        o.write( new_line )


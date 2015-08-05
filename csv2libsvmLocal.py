#!/usr/bin/env python

"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.
"""

import sys
import csv

def construct_line( label, line ):
new_line = []
if float( label ) == 0.0:
    label = "0"
new_line.append( label )

for i, item in enumerate( line ):
    if item == '' or float( item ) == 0.0:
        continue
    new_item = "%s:%s" % ( i + 1, item )
    new_line.append( new_item )
new_line = " ".join( new_line )
new_line += "\n"
    return new_line

# --

input_file = 'titles.csv'
output_file = 'titles.svm'
label_index = -1
skip_headers = 0
pivot = 1

i = open( input_file )
o = open( output_file, 'wb' )

reader = csv.reader( i )
if skip_headers:
    reader = reader.next()

 # pivot column "pivot"
if pivot > -1:
    piv = {}
    for line in reader:
        # if not piv.has_key(line[pivot]): piv[ line[pivot] ] = {}
        # piv[ line[pivot] ][ line[ int(not pivot) ] ] = 1.0
        if not piv.has_key(line[pivot]): piv[ line[pivot] ] = []
        piv[ line[pivot] ][ int(line[ int(not pivot) ]) ] = 1.0
    reader = piv.values()
# --

for line in reader:
    if label_index == -1:
        label = "1"
    else:
        label = line.pop( label_index )
        
    new_line = construct_line( label, line )
    o.write( new_line )


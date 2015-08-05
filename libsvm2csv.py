#!/usr/bin/env python

"""
convert libsvm file to csv'
libsvm2csv.py <input file> <output file> <X dimensionality> [<labels file>]
"""

import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

d = int( sys.argv[3] )
assert ( d > 0 )

index_file = sys.argv[4]
index = {}

reader = csv.reader( open( input_file ), delimiter = " " )
writer = csv.writer( open( output_file, 'wb' ))


if index_file: # add header row with the provided dictionary keys
	for row in csv.reader(open( index_file )):
		index[row[1]] = row[0]

	header_line = ['target']
	for k,v in sorted(index.iteritems(), key=lambda(k,v): int(k)):
		if len(header_line) < d: header_line += [v]

	# print header_line
	writer.writerow( header_line )


for line in reader:
	label = line.pop( 0 )

	if label in index:
		label = index[label]

	if line[-1].strip() == '':
		line.pop( -1 )

	# print line

	line = map( lambda x: tuple( x.split( ":" )), line )
	#print line
	# ('1', '0.194035105364'), ('2', '0.186042408882'), ('3', '-0.148706067206'), ...

	new_line = [ label ] + [ 0 ] * (d - 1)
	for i, v in line:
		i = int( i )
		if i < d:
			new_line[i] = v

	writer.writerow( new_line )

#! /usr/bin/python

# 
#  maltminder.py
#  maltminder
#
#  Search NC Spiritous Liquor Pricebook from the command line.
#
#  Created by Jay Roberts on 2012-04-05.
# 

import csv
import sys
import string
import locale

locale.setlocale(locale.LC_ALL, '')

def printEntry(entry):
    sys.stdout.write('%s %s' % (locale.currency(float(entry['price'])), entry['name']))
    sys.stdout.write("\n")
    sys.stdout.flush()

if __name__ == '__main__': 
    path = 'data/nc_quarterly_pricing.csv'

    spiritReader = csv.reader(open(path, 'r'))

    spiritData = []


    try:
        term = sys.argv[1]
        term = term.lower()
    except:
        term = None
        sys.stdout.write("Displaying all entries:\n")
        sys.stdout.flush()

    for line in spiritReader:
        if term == None or term in line[2].lower():
            entry = dict()
            entry['distiller'] = line[1]
            entry['name']      = line[2]
            entry['age']       = line[3]
            entry['proof']     = line[4]
            entry['size']      = line[5]
            entry['price']     = line[6]
            
            printEntry(entry)
    
#! /usr/bin/python


import csv
import sys
import string

def printEntry(entry):
    sys.stdout.write('%s %s %s %s' % (entry['name'], entry['age'], entry['proof'], entry['price']))
    sys.stdout.write("\n")
    sys.stdout.flush()

if __name__ == '__main__': 
    path = 'data/nc_quarterly_pricing.csv'

    spiritReader = csv.reader(open(path, 'r'))

    spiritData = []

    term = sys.argv[1].lower()

    for line in spiritReader:
        if term in line[2].lower():
            entry = dict()
            entry['distiller'] = line[1]
            entry['name']      = line[2]
            entry['age']       = line[3]
            entry['proof']     = line[4]
            entry['size']      = line[5]
            entry['price']     = line[6]
            
            printEntry(entry)
    
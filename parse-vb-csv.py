#!/usr/bin/python3

import csv
import sys

def openCSV(filename):
    with open(filename, 'rt') as f:
        i = 0
        # decimal is set to comma to represent german number format
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            # print the first line without evaluation of the 19th column
            if(len(row) > 19):
                if(row[19] == "Betrag"):
                    concatColumn(row,0,4,";")
                    concatColumn(row,5,17," ")
                    concatColumn(row,18,18,";")
                else:
                    concatColumn(row,0,4,";")
                    concatColumn(row,5,17," ")
                    concatColumn(row,18,18,";")
                    # if negative value put in 19th column otherwise the 20th
                    # for the comparison replace comma with point
                    if(toFloat(row[19])< 0):
                        print(row[19]+";", end='')
                    else:
                        print(";"+row[19], end='')
                print(";"+row[20], end='\n')
            else:
                i = i+1
                print(str(i)+" lines were omitted\n")

def toFloat(str):
    s = str.replace('.','')
    s = s.replace(',','.')
    return float(s)

def concatColumn(row, start, end, delimiter):
    for i in range(start, end):
        print(row[i]+delimiter,end='')

l = len(sys.argv)
for x in range(len(sys.argv)):
    if x !=0:
        openCSV(sys.argv[x])

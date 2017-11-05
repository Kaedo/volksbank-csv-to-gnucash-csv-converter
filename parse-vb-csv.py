#!/usr/bin/python3

import csv
import sys

def openCSV(filename):
    with open(filename, 'rt') as f:
        i = 0
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            # if we do not have 21 columns in the line skip it
            if(len(row) > 21):
                # print the first line without evaluation of the 19th column
                if(row[19] == "Betrag"):
                    concatColumn(row,0,4,";")
                    concatColumn(row,5,17," ")
                    concatColumn(row,18,18,";")
                else:
                    concatColumn(row,0,4,";")
                    concatColumn(row,5,17," ")
                    concatColumn(row,18,18,";")
                    # split the positive and negative values in different columns
                    # if negative value put in 19th column otherwise the 20th
                    # for the comparison replace comma with point and convert to float
                    if(toFloat(row[19])< 0):
                        print(row[19]+";", end='')
                    else:
                        print(";"+row[19], end='')
                print(";"+row[20], end='\n')
            else:
                # count the omitted lines
                i = i+1
                print(str(i)+" lines were omitted\n")

# decimal is set to comma to represent german number format
# convert '2.100,30' to 2100.30
def toFloat(str):
    s = str.replace('.','')
    s = s.replace(',','.')
    return float(s)

# used to merge the columns which are descriptions (verwendungszweck)
def concatColumn(row, start, end, delimiter):
    for i in range(start, end):
        print(row[i]+delimiter,end='')

# for each argument (file) which is not this python script, start converting
l = len(sys.argv)
for x in range(len(sys.argv)):
    if x !=0:
        openCSV(sys.argv[x])

#-------------------------------------------------------------------------------
# Name:        csvCutter
# Purpose:
#
# Author:      gmarketos
#
# Created:     05/07/2013
# Copyright:   (c) gmarketos 2013
# Licence:     MIT
#-------------------------------------------------------------------------------
import csv
import sys

delimiterChar=','
quoteChar='"'
columnsFile = 'columns.csv'
inputFile = 'a.csv'

def main(argv):
    for i in range (0, len(argv)):
        if (argv[i] == '-cFile'):
            global columnsFile
            columnsFile=argv[i+1]
            print ("Columns file= "+columnsFile)
        elif (argv[i] == '-iFile'):
            global inputFile
            inputFile=argv[i+1]
            print ("Input file= "+inputFile)
        ##elif (argv[i] == '-qChar'):
        ##    global quoteChar
        ##    quoteChar=argv[i+1]
        ##    print ("Quote character= "+quoteChar)	
			
    fileReader()


def columnsReader():
    with open(columnsFile, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiterChar, quotechar=quoteChar)
        for colsToBeSelected in spamreader:
            return colsToBeSelected;


def fileReader():
    #retrieves the list of columns to be selected
    colsToBeSelected = columnsReader();

    
    with open(inputFile, 'rt') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiterChar, quotechar=quoteChar)
     #retrieves the first row (columns) of the input file
        for row in spamreader:
            cols = row;
            break;

        i=-1
        listOfColNums = [];
        exportedCols = [];
        for col in cols:
            i=i+1
            if any(col in s for s in colsToBeSelected):
                exportedCols.append(col);
                listOfColNums.append(i)

        csvfile = open(inputFile+'.output.csv', 'wt')
        csvwriter = csv.writer(csvfile, delimiter=delimiterChar, quotechar=quoteChar, lineterminator='\n')
        csvwriter.writerow(exportedCols)

        rws = [];        
        for row in spamreader:
             
              newRow=[]
              for colNum in listOfColNums:
                   newRow.append(row[colNum])
              rws.append(newRow)  

        csvwriter.writerows(rws)
            

if __name__ == '__main__':
    main(sys.argv[1:])

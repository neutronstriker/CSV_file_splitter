# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:53:33 2017

@author: Srinivas N

Description : Splits a file into number of parts specified by user based on number of lines
present in the file, however we could also try the size of file to decide which line to
split at.

Microsoft Excel (R) has a limitation that it can have only 1048576(2^20) line numbers max if you try
to open a CSV file. If your file has more than that many lines the file opens but it will get truncated.

So this utility was designed to break large CSV files into smaller chunks, so that it can be opened
by Excel for analysis.
"""
import sys

def linesInFile(fileName):
    f = open(fileName,'r')    
    i = 0
    for next in f:
        i=i+1
    f.close()
    return i

def splitFiles(masterFileName,splitCount):
    splitNumber=1
    fmaster  = open(masterFileName,'r')
    linesInMasterFile = linesInFile(masterFileName)
    splitAt = linesInMasterFile/splitCount
    while splitNumber <= splitCount:
        outFile = open(masterFileName.split('.')[0]+'_'+str(splitNumber)+'.'+masterFileName.split('.')[1],'w')
        i = 0
        for next in fmaster:
            if i < splitAt:
                outFile.write(next)
                i = i+1
            else:
                break
        outFile.close()
        sys.stdout.write('.')
        #j = j+splitAt
        splitNumber = splitNumber+1
    if outFile.closed is False:
        outFile.close()
        
if __name__ == '__main__':
    print 'CSV File Splitter v1.0, Author: Srinivas N'
    print 'This program will split a large CSV file into smaller chunks.'
    print 'Please enter the name and path of file you want to split:'
    print ':>',
    filename = raw_input()
    print 'Please enter the number of pieces you want to make of it:'
    print ':>',
    splitCount = raw_input()
    try:
        splitCountNum = int(splitCount)
    except ValueError:
        print 'Invalid number entered, exiting..'
        raw_input()
        sys.exit(0)
    try:
        print 'Please wait, splitting now....',
        splitFiles(str(filename),splitCountNum)
        print '\nSplitting Complete, press enter to exit'
        raw_input()
    except Exception as e:
        print '\nThere has been an exception, please make sure the "'+str(filename)+'" is the correct filename and is not locked by any other application.'
        print 'Find the error details below..'
        print str(e)
        raw_input()
        sys.exit(0)
        

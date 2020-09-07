#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#week1 assignment2

import urllib2
import csv
import datetime
import logging
import argparse
import sys

#Part2 : Download DATA
def downloadData (url):
    """Takes in a string called url.Purpose: to download contents located at url and return to caller.

    Args:
        url(str): the url to be call/open

    Returns:
        userfile : infomation from the data in URL.

    Examples:
         >>> downloadData(https:www.wikipedia.com)
    """
   userfile = urllib.urlopen(url)
   return userfile

#_________________________________________________________________________________________________
#Part3 : Process Data
def processData(userfile):
    """Process data from file line by line.

    Args:
        userfile(csv) : A .csv file

    Returns:
        userdict(dict): A dictionary that maps person's ID to a TUPLE of form (name, birthday)

    Example:
        >>>

    """

read_file = csv.DictReader (userfile)
person_dict = {}

    for (line, col) in enummeerate(read_file):
        try:
            person_dict[col[0]] = (col[1], datetime.datetime.strptime (col[2],'%d/%m/%Y').date())
        except:
            logger.error("Error processing line #{} for ID#{}".format(line,col[0]))

    return person_dict

#_________________________________________________________________________________________________
#Part4 : Display/ User Input  
def displayPerson (id, personData):
    """ To display a person's informatioin

        Args:
            id(int) : A user's ID
            personData(dict) : Dictionary containing member info
    """
    
    id = str (id)

    if id not in personData.keys():
        print("No user found with that id")
    else:
        print ("Person #{} is {} with a birthday of {}".format
               (id,personData[id][0], personData[id][1].strftime('%Y-%m-%d')))

#_____________________________________________________________________________________________________
#Part5 : Putting it all together. using argparse module
def main():
    """ A function to be called when the program runs."""

    parser = argparse.ArgumentParser()
    parser.add_argument("--url",help="URL of CSV to download")
    args = parser.parse_args()

    if args.url:
        try:
            csvData = downloadData(args.url)
        except urllib2.URLError:
            print ("Can't retrieve, please check and try the URL again")
            sys.exit()

        personData = processData (csvData)

        try:
            id = int (input ("Please enter the user ID:  " ))
            if id <= 0:
                print ("You've entered a number(<= 0),program will quit")
                sys.exit()
            else:
                displayPerson(id, personData)
                main()

        except ValueError:
            print ("Enter a valid user ID")
            sys.exit()

    else:
        print ("Plese check the requirement of URL parameters")
        sys.exit()
                                     

if __name__ == '__main__':
    main()

#!/usr/bin/python
"""
Log Anonymizer

TL;DR:
        Hashes IP, IDENT, and User fields in the
            Common Log Format
            Common Log Format with Virtual Host
            NCSA Extended/Combined log format
            
About:
        Usecase is to generate log files that do not reveal
        user identifiable information, but can be used for
        analytics.  The idea is to supply the log file, read lines,
        hash the desired fields using hashlib and a random
        or user supplied salt, and output the file as specified
        by the user.

Disclaimer:
        I am not a cryptographer nor an infrmation privacy
        specialist.  This is a best effort project and should
        be classified with all the other 'I'm doing this to learn Python"
        projects that exist on the web.
        That said, pointers for self-improvement are ALWAYS welcome.
        Toss them my way at <email address TBD>
        
Thank you:
    Harry Fuecks for the Apache log heavy lifting.  Saving me from having to
    wimp out or enter what would surely be a losing regex battle.
    - https://pypi.python.org/pypi/apachelog/
    
    Peter Hickman for Apache::LogEntry (Perl) so that Harry could port it to Python. 
"""
import argparse
import os.path
import sys
 
def check_files(input, output):
    '''
    Check if input file exists and is in the right format
    Check if output file exists and ask how to handle
    
    '''
    
    if os.path.exists(input):
        print ("Input file %s exists" % input)
    else:
        sys.exit('Input file does not exist')
    #open input file and check is log file
    
    if os.path.exists(output):
        print ("Output file: %s exists" % output)
        kbd = raw_input('Would you like to overwrite, append or quit? <o/a/q>' )
        
        while (kbd != 'o') and (kbd != 'a') and (kbd != 'q'):
             kbd = raw_input('Would you like to overwrite, append or quit? <o/a/q>' )
            
        if (kbd == 'o'):
            return kbd
        elif (kbd == 'a'):
            return kbd
        elif (kbd == 'q'):
           sys.exit("Exiting...")
        else:
             sys.exit('invalid input & aborting')
    else:
        return 'a'
    
        
def hashomatic():
    stuff


def file_processor():
    kbd = raw_input('Would you like to overwrite, append or quit? <o/a/q>' )
        
    while (kbd != 'o') and (kbd != 'a') and (kbd != 'q'):
         kbd = raw_input('Would you like to overwrite, append or quit? <o/a/q>' )
        
    if (kbd == 'o'):
        print "overwrite"
    elif (kbd == 'a'):
        print "append"
    elif (kbd == 'q'):
       sys.exit("Exiting...")
    else:
         sys.exit('invalid input & aborting')
            

def main():
    verify_files = check_files(args.input, args.output)
    print verify_files
    
 #Main
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log Anonymization Processor')
    parser.add_argument('-i','--input', help='Source CLF log file',required=True)
    parser.add_argument('-o','--output',help='Destination Anonymized log file', required=True)
    parser.add_argument('-s','--secret',help='Secret Key', required=False)
    args = parser.parse_args()
 

    inputFile = args.input
    outputFile = args.output

    main()
    
    
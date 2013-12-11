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
        I am not a cryptographer nor an information privacy
        specialist.  This is a best effort project and should
        be classified with all the other 'I'm doing this to learn Python"
        projects that exist on the web.
        That said, pointers for self-improvement are ALWAYS welcome.
        Toss them my way at <email address TBD>
        
Thank you:
    Harry Fuecks for the Apache log heavy lifting.  Saving me from having to
    wimp out or enter what would surely be a losing regex battle.
    - https://pypi.python.org/pypi/apachelog/
    
    Peter Hickman for Apache::LogEntry (Perl) so that Harry could port it to Python. :D
"""
import argparse
import os.path
import sys
import random
import hashlib
import string
import apachelog
import pdb


    
def gen_random():
    '''Generate random string 
    '''
    char_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
    var_chars = random.sample(char_set, 24)
    
    return ''.join(var_chars) 


class LogFile(object):
    '''
    What do we want from our file class?
    Input, output, lines processed, lines not processed, line total
    '''
    def __init__(self, **kwargs):   
        self.file_input = kwargs.get('input', '') 
        self.file_output = kwargs.get('output', '')
        self.write_mode = None  
        self.log_format = kwargs.get('format')
        self.hash_salt = kwargs.get('secret')
        self.lines_accepted = 0
        self.lines_rejected = 0
        
        if self.hash_salt is None:
            self.hash_salt = gen_random()
        
        if self.write_mode is None:
            self.check_files()
        
        if self.log_format is None:
            self.log_format = apachelog.formats['extended'] #changed from deault of 'extended'
        
        #pdb.set_trace()
       
    def line_accept(self):
        self.lines_accepted += 1    
    
    def line_regect(self):
        self.lines_rejected += 1
    
    
    def check_files(self):
        '''
        Check if input file exists and is in the right format
        Check if output file exists and ask how to handle
        
        
        Probably will end up hating this implemntation.
        think that there's no output class which is where writemode
        would really belong. we can probably make good assumptions
        to get the behavior to make sense off of just input file.
        '''
        
        if os.path.exists(self.file_input):
            print ("Input file %s exists" % self.file_input)
        else:
            sys.exit('Input file does not exist')
        #open input file and check is log file
        
        if os.path.exists(self.file_output):
            print ("Output file: %s exists" % self.file_output)
            kbd = raw_input('Would you like to overwrite, append or quit? <o/a/q>' )
            
            while kbd.lower() not in ['o', 'a', 'q']:
                 kbd = raw_input('Would you like to overwrite, append or quit? <o/a/q>' )
                
            if (kbd.lower() == 'o'):
                self.write_mode = 'w'
            elif (kbd.lower() == 'a'):
                self.write_mode = 'a'
            elif (kbd.lower() == 'q'):
               sys.exit("Exiting...")
            else:
                sys.exit('invalid input & aborting')  #should probably raise an actual error
        else:
            self.write_mode = 'w'

def hashomatic(string_val, hash_salt):
    '''receives format string value & salt. returns hash
    '''
    #pdb.set_trace()
    hash_string = hashlib.md5(string_val + hash_salt).hexdigest()
    
    return hash_string

def hash_log_line(read_line, log_job):
    parser = apachelog.parser(log_job.log_format)
    try:
        log_line = parser.parse(read_line)
        anon_order.lines_accepted += 1
    except apachelog.ApacheLogParserError:
        anon_order.lines_rejected += 1
        #pdb.set_trace()
    hash_keys = ['%h', '%a', '%u', '%l']
        #pdb.set_trace()   #check if value is a - and skip the hashing because it's not needed            
    while hash_keys:
        hash_key = hash_keys.pop()
        if hash_key in log_line.keys():
            if log_line[hash_key] == '-':
                pass
            else:
                log_line[hash_key] = hashomatic(log_line[hash_key], anon_order.hash_salt)
    return log_line          


#Main
def main():
    '''Check files, setup log file object,
    process line,
    assemble output file
    '''
    anonymize_order = LogFile(**args)
    source_file = open(anonymize_order.file_input, 'r')
    destination_file = open(anonymize_order.file_output, anonymize_order.write_mode)
    parser = apachelog.parser(anonymize_order.log_format)
    
    read_line = 1
    while read_line:
        read_line = source_file.readline()
        #pdb.set_trace()
        #log_line = hash_log_line(read_line, anon_order)          
        try:
            log_line = parser.parse(read_line)
            anonymize_order.lines_accepted += 1
        except apachelog.ApacheLogParserError:
            anonymize_order.lines_rejected += 1
        #pdb.set_trace()
        hash_keys = ['%h', '%a', '%u', '%l']
        #pdb.set_trace()   #check if value is a - and skip the hashing because it's not needed            
        while hash_keys:
            hash_key = hash_keys.pop()
            if hash_key in log_line.keys():
                if log_line[hash_key] == '-':
                    pass
                else:
                    log_line[hash_key] = hashomatic(log_line[hash_key], anonymize_order.hash_salt)

        #need to reorder the writeline back to the log format
        log_order = anonymize_order.log_format.split()
        log_order = [format_key.replace('\\', '') for format_key in log_order]
        log_order = [format_key.replace('"', '') for format_key in log_order]
        write_line = []
        for format_key in log_order:
            write_line.append(log_line[format_key])

            #pdb.set_trace()
        write_line.append('\n')
        write_line = ' '.join(write_line)
        destination_file.write(write_line)
    
            #write_line = hashomatic(read_line, anon_order.log_format)
            #print write_line
            #parser = apachelog.parser(anon_order.log_format)
            
        
            #open file
            #read lines
            #hashit
            #assemble
            #write file
    print 'Lines accepted: ' + str(anonymize_order.lines_accepted)
    print 'Lines rejected: ' + str(anonymize_order.lines_rejected)
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Log Anonymization Processor')
    parser.add_argument('-i','--input', help='Source CLF log file',required=True)
    parser.add_argument('-o','--output',help='Destination Anonymized log file', required=True)
    parser.add_argument('-s','--secret',help='Secret Key', required=False)
    parser.add_argument('-f','--format',help='Log Format', required=False)
    args = vars(parser.parse_args())
 
    main()
    
    
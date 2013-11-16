PyLogAnonymizer
===========

About
------
PyLogAnonymizer will be a utility to anonymize Apache log files.

Usage
------
You will need to pass two required command line arguments:
    * -i     input log file
    * -o    output log file
    * -s    secret key (aka your own salt) - optional

Other Stuff
----------
Regarding the secret key.  If you do not supply a key,  one will be generated at random for
use within that run of the script.  You will need to supply a key of your own
if you wish your output to be comparable with multiple sets generated from this script.

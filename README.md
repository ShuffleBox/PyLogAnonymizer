PyLogAnonymizer
===========

About
------
PyLogAnonymizer will be a utility to anonymize Apache log files.

Usage
------
You will need to pass two required command line arguments:

`
-i input log file
`

`
-o output log file
`

`
-s secret key (optional)
`

Other Stuff
----------
Regarding the secret key.  If you do not supply a key,  one will be generated at random for
use within that run of the script.  You will need to supply a key of your own
if you wish your output to be comparable with multiple sets generated from this script.

Example:

192.168.1.150 could hash to `e1c8d6347c0c24e5cbc60e508f3fc1b5` one run and '2d89bb609f74f6df0be8578de2fe5184' the next, breaking some use cases such as analytics.
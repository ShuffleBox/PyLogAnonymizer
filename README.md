PyLogAnonymizer
===========

About
------
PyLogAnonymizer is a utility to anonymize Apache log files.  It is designed to parse and hash the Apache Common Log Format
and write the output to the specified file.

Usage
------
usage: pyloganonymizer.py [-h] -i INPUT -o OUTPUT [-s SECRET] [-f FORMAT]

Command line arguments:

`
-i input log file
`

`
-o output log file
`

`
-s secret key (optional)
`

`
-f specify log format
`

Example
------
`
hostname:~/dev/PyLogAnonymizer/> python pyloganonymizer.py -i login.txt -o logout.txt
Input file 100.txt exists
Lines accepted: 100
Lines rejected: 1
`

`
loginput.txt
192.168.1.135 - - [02/Apr/2013:19:00:27 -0500] "GET /sites/default/files/css/some.css HTTP/1.1" 200 10850 "http://www.example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17"
192.168.1.135 - - [02/Apr/2013:19:00:27 -0500] "GET /sites/default/files/css/some2.css HTTP/1.1" 200 5213 "http://www.example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17"
192.168.2.110 - - [02/Apr/2013:19:00:27 -0500] "GET /sites/default/files/css/some.css HTTP/1.1" 200 1801 "http://www.example.com/" "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
`

`
logoutput.txt
<...>
b10a30232e8a174a4692e4e99caacfe3 - - [02/Apr/2013:19:00:27 -0500] "GET /sites/default/files/css/some.css HTTP/1.1" 200 10850 "http://www.example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17" 
b10a30232e8a174a4692e4e99caacfe3 - - [02/Apr/2013:19:00:27 -0500] "GET /sites/default/files/css/some2.css HTTP/1.1" 200 5213 "http://www.example.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17" 
2393be6fdc6d870ccbdc0af1518ffad8 - - [02/Apr/2013:19:00:27 -0500] "GET /sites/default/files/css/some.css HTTP/1.1" 200 1801 "http://www.example.com/" "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" 
<...>
`

Other Stuff
----------
Regarding the secret key.  If you do not supply a key,  one will be generated at random for
use within that run of the script.  You will need to supply a key of your own
if you wish your output to be comparable with multiple sets generated from this script.

Example:

192.168.1.150 could hash to `e1c8d6347c0c24e5cbc60e508f3fc1b5` one run and `2d89bb609f74f6df0be8578de2fe5184` the next, breaking some use cases such as analytics.
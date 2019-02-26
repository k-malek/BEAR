# BEAR v. 0.3
Uniaxial streching test data analyzer.

# What is BEAR for?

BEAR is a program which analyzes data out of uniaxial streching test and provides user with plot and data: tensile strength - Rm, yield point - R 0.2 and modulus - E.

# How to use it?
Using BEAR is fairly easy for Python3 users. First of all you have to download matplotlib library for Python. Place the COPY (read Notes down below) of your file into folder with your bear.py file. Run bear.py. Insert full name of your file (e.g. "2017_X15_700C.xls"). Give BEAR couple of seconds :). BEAR will provide you with first plot. Your job is to judge the trend line on the left. If everything is ok - that's also your final plot. Close the chart - program will ask you whether trend line was good or bad. If you choose "t" for "yes" option you will be provided with bearing data: Re, Rm and E. If you choose "n" for "no" then you will be asked for two points from your data: starting and ending point of which program will prepare new trend line (don't worry! You will be asked about it as many time as needed, so you can try out different combinations until your satisfied with results).

# Notes
For now there's only Polish language version of BEAR, yet english one is going to appear soon. Be careful! What program actually does is it cuts all unnecessery things for it leaving only data. Make sure you make backup for your file before giving it to BEAR :) Feel free to use my three test files. Especialy first one (500C), which is disasterous enough to be helpful with gettin hang of BEAR mechanics :)

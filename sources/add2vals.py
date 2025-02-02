'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    print("")
    print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
    print("")
    sys.exit(0)

    
if argnumbers == 3 :
    print("")
    print("The result is " + str(calc.multiply3(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))))
    print("")
    sys.exit(0)

if argnumbers !=2 and argnumbers != 3:
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")
    print("Usage: 'add2vals X Y ' or 'multiply3vals X Y Z' where X and Y or Z are individual values.")
    print("       If add2vals or multiply3vals is not in your path, usage is './add2vals X Y' or './multiplyvals X Y Z'.")
    print("       If unbundled, usage is 'python add2vals.py X Y'." 'python add2vals.py X Y Z'.")
    print("")
    sys.exit(1)
 



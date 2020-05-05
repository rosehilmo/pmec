

import numpy as np
import pickle
import argparse
import os
from os import path

"""
Call from command line Example: "python3 np_arg_assignment.py -x 3 5 2 4 6 3 -y 6 -v add"
Can be any combination of numbers after -x
Can be any integer after -y
Can be one of 5 choices after -v, add, subtract, multiply, divide, or exponent
   
"""

outputfolder='np_arg_assignment_output'

#makes folder if does not exist
if path.exists(outputfolder) == False:
    os.mkdir(outputfolder)

filename='results.pickle'
outfile=open(outputfolder + '/' + filename,'wb')

#Defines argparse arguments

parser = argparse.ArgumentParser()
parser.add_argument('-x','--x',nargs='+',type=int,help='<Required> Set flag', required=True)
parser.add_argument('-y','--y',type=int,help='input number operate on list')
parser.add_argument("-v","--verbosity", type=str, 
        choices=['add','subtract','multiply','divide','exponent'],help='choose operand')
args=parser.parse_args()

#Runs whichever argument chosen in argparse arguments
if args.verbosity == 'add':
    answer=np.add(np.array(args.x),args.y)
    print('Elementwise sum equals' + str(answer))

if args.verbosity == 'subtract':
    answer=np.subtract(np.array(args.x),args.y)
    print('Elementwise difference equals' + str(answer))

if args.verbosity == 'multiply':
    answer=np.multiply(np.array(args.x),args.y)
    print('Elementwise product equals' + str(answer))

if args.verbosity == 'divide':
    answer=np.divide(np.array(args.x),args.y)
    print('Elementwise quotient equals' + str(answer))

if args.verbosity == 'exponent':
    answer=np.array(args.x)**args.y
    print('Elementwise quotient equals' + str(answer))


#puts resutls in output file and folder
pickle.dump(answer,outfile)
outfile.close()
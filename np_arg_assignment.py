

import numpy as np
import pickle
import argparse

filename='results.pickle'
outfile=open(filename,'wb')

parser = argparse.ArgumentParser()
parser.add_argument('-x','--x',nargs='+',type=int,help='<Required> Set flag', required=True)
parser.add_argument('-y','--y',type=int,help='input number operate on list')
parser.add_argument("-v","--verbosity", type=str, 
        choices=['add','subtract','multiply','divide','exponent'],help='choose operand')
args=parser.parse_args()

#import pdb; pdb.set_trace()
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



pickle.dump(answer,outfile)
outfile.close()
import numpy as np
import scipy.signal as signal
import sys
from tools import unshape

NA = np.newaxis

def runave(rdata, length):
    """runnnig average
    
    Arguments:

       'array'  -- first dimension must be time. 

       'length' -- runnning mean length

    """
    ntim = rdata.shape[0]
    if ntim < length:
        print "input array first dimension length must be larger than length."
        sys.exit()        

    if rdata.ndim == 1:
        if length%2 != 0:
            w = np.ones(length)/float(length)
        else:
            w = np.r_[0.5, np.ones(length-1), 0.5]/float(length)                
        runarray = np.ma.array(signal.convolve(rdata, w, 'same'))
        runarray[:length/2] = np.ma.masked
        runarray[-length/2:] = np.ma.masked
    elif rdata.ndim == 2:
        if length%2 != 0:
            w = np.vstack((np.zeros(length),np.ones(length),np.zeros(length)))/float(length)
        else:
            w = np.vstack((np.zeros(length+1),np.r_[0.5, np.ones(length-1), 0.5],\
                           np.zeros(length+1)))/float(length)
        runarray = np.ma.array(signal.convolve2d(rdata, w, 'same'))
        runarray[:length/2,:] = np.ma.masked
        runarray[-length/2:,:] = np.ma.masked
    else :
        rdata, oldshape = unshape(rdata) 
        if length%2 != 0:
            w = np.vstack((np.zeros(length),np.ones(length),np.zeros(length)))/float(length)
        else:
            w = np.vstack((np.zeros(length+1),np.r_[0.5, np.ones(length-1), 0.5],\
                           np.zeros(length+1)))/float(length)
        runarray = np.ma.array(signal.convolve2d(rdata, w, 'same'))
        runarray[:length/2,:] = np.ma.masked
        runarray[-length/2:,:] = np.ma.masked
        runarray = runarray.reshape(oldshape)

    return runarray

def regression(x, y):
    """
    regression y = ax + b
    """
    if x.ndim != 1:
        print "error x must be 1-D array"
        sys.exit()
    if y.ndim >= 2:
        y, oldshape = unshape(y)
        p = np.polyfit(x,y,1)
        a = p[0].reshape(oldshape[1:])
        b = p[1].reshape(oldshape[1:])
    else:
        p = np.polyfit(x,y,1)
        a = p[0]
        b = p[1]

    return a, b

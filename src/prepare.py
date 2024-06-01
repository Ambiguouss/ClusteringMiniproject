import numpy as np
import os
from model import *
from Hierarchical import *

def prepare2D(data):
    X=data[:,:-1]
    Y=data[:,-1].astype(int)
    Y-=1
    return X,Y
def preparerp(data):
    X=data[:,:-1]
    Y=data[:,-1]
    Y=np.where(Y==2,0,1)
    return X,Y

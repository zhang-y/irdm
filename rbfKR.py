from sklearn.metrics.pairwise import rbf_kernel
import numpy as np


def predict(X,y,gamma):
        
    K = rbf_kernel(X.reshape(-1,1),X.reshape(-1,1),gamma)
    pred = (K * y[:, None]).sum(axis=0) / K.sum(axis=0)
        
    return pred
        
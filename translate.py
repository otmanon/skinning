import numpy as np

def translate(t):

    A = np.zeros((3, 4))
    A[:, 0:3] = np.eye(3)
    A[0, 3] = t[0]
    A[1, 3] = t[1]
    A[2, 3] = t[2]

    return A
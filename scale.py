import numpy as np


def scale(s):
    """
    Build the affine matrix that performs scaling with parameters sx, sy, sz
    """
    A = np.zeros((3, 4))
    A[0, 0] = s[0]
    A[1, 1] = s[1]
    A[2, 2] = s[2]

    return A
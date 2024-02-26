import numpy as np
from rotate import rotate



def slerp(r1, r2, s):
    """
    Interpolates two affine matrices A1 and A2 with parameter s
    """
    r1 = np.array(r1)
    r2 = np.array(r2)
    r = (1 - s) * r1 + s * r2
    R = rotate(r)
    return R
import numpy as np
import scipy as sp
from scipy.spatial.transform import Rotation as rot

def rotate(a):
    """
    Build the affine matrix that performs rotation axis angle vector a
    """
    A = np.zeros((3, 4))

    R = rot.from_rotvec(a).as_matrix()
    A[0:3, 0:3] = R

    return A
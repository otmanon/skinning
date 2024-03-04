import numpy as np
def lbs(X0, W, T):
    # Perform linear blend skinning on the mesh X0, with a list of b skinning weights W, and a list of b affine matrices T
    b = W.shape[1]
    X = np.zeros((X0.shape[0], 3))

    ### sum over all affine matrices b, their contributions to x.
    for j in range(b):
        xd =  W[:, j] * (T[j] @ X0.T)
        X += xd.T
    return X
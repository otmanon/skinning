import numpy as np

def linear_blend_skinning(X0, W, T):
    """
    Performs Linear blend skinning

    Parameters
    ----------
    V : np.ndarray
        Vertices of the mesh
    X0 : np.ndarray
        Rest pose of the mesh
    W : np.ndarray
        Weights of the mesh
    T : np.ndarray
        b x 3 x 4 affine trnasformations of the mesh

    Returns
    -------
    X : np.ndarray
        Deformed vertices of the mesh
    """
    if T.ndim == 2:
        T = T.reshape(1, T.shape[0], T.shape[1])
    n = X0.shape[0]
    dim = X0.shape[1]

    X = np.zeros((n, dim))
    for b in range(T.shape[0]):
        Tb = T[b]
        for i in range(n):
            w = W[i, b]
            x0 = np.array([X0[i, 0], X0[i, 1], X0[i, 2], 1])
            x = w * Tb @ x0
            X[i] += x

    return X




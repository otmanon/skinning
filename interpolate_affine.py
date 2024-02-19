


def interpolate_affine(A1, A2, s, t):
    """
    Interpolates two affine matrices A1 and A2 with parameter s
    """
    return (1 - s/t) * A1 + s/t * A2
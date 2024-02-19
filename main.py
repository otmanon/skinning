import numpy as np
import polyscope as ps
import igl

from scale import scale
from translate import translate
from rotate import rotate
from slerp  import slerp
from keyframe_animate import keyframe_animate


## Load a mesh from our computer
[X, _, _, F, _, _]  = igl.read_obj("./data/snail.obj")
# Create a set of uniform skinning weights
W = np.ones((X.shape[0], 1))

## Scale the mesh
s1 = [1, 1, 1]
s2 = [3, 3, 3]
A1 = scale(s1)
A2 = scale(s2)

t1 = [0, 0, 0]
t2 = [0, 1, 0]
A3 = translate(t1)
A4 = translate(t2)

r1 = [0, 0, 0]
r2 = [0, 0, np.pi/2]
r3 = [0, 0, -np.pi/2]
A5 = rotate(r1)
A6 = rotate(r2)
A7 = rotate(r3)



## Perform keyframe animation
keyframe_animate(X, F, A1, A2, W,  50)

keyframe_animate(X, F, A2, A3, W,  10)

keyframe_animate(X, F, A3, A4, W, 100)

keyframe_animate(X, F, A4, A5, W, 50)

keyframe_animate(X, F, A5, A6, W, 50)


keyframe_animate(X, F, A6, A7, W, 50)
# now go from A7 to A6 again but with way smaller angles
timesteps = 100
A_next = A7.copy()
for i in range(timesteps):
    A_prev = A_next.copy()
    A_next = slerp(r3, r2, i, timesteps)
    keyframe_animate(X, F, A_prev, A_next, W, 1)



import numpy as np
import polyscope as ps
import time

from lerp import lerp
from linear_blend_skinning import linear_blend_skinning
def keyframe_animate(X, F,  A1, A2, interp, num_timesteps, fps=120):
    ps.init()
    ps.remove_all_structures()
    ps_mesh = ps.register_surface_mesh("mesh", X, F)
    ps.set_ground_plane_mode("none")
    ps.set_give_focus_on_show(True)
    W = np.ones((X.shape[0], 1))
    for i in range(num_timesteps):
        A = interp(A1, A2, i, num_timesteps)
        V = linear_blend_skinning(X, W, A)
        ps_mesh.update_vertex_positions(V)
        ps.frame_tick()

        time.sleep(1/fps)



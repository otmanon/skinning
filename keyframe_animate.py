import polyscope as ps
import time

from lerp import lerp
from linear_blend_skinning import linear_blend_skinning

def keyframe_animate(X, F,  A1, A2, W, num_timesteps, fps=120):
    ps.init()
    ps_mesh = ps.register_surface_mesh("mesh", X, F)
    ps.set_ground_plane_mode("none")

    for i in range(num_timesteps):

        A = lerp(A1, A2, i, num_timesteps)
        V = linear_blend_skinning(X, W, A)
        ps_mesh.update_vertex_positions(V)
        ps.frame_tick()

        time.sleep(1/fps)



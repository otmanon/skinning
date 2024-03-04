import numpy as np
import polyscope as ps
def animate(X, F, W, P, lbs):
    ps.remove_all_groups()
    ps.remove_all_structures()
    X01 = np.hstack((X, np.ones((X.shape[0], 1))))
    for t in range(P.shape[0]):
        p = P[t, :, :, :]

        X = lbs(X01, W, p)
        if t == 0:
            ps.init()
            mesh = ps.register_surface_mesh("mesh", X, F, edge_width=1)
            ps.reset_camera_to_home_view()
        else:
            mesh.update_vertex_positions(X)
            ps.frame_tick()
        mesh.update_vertex_positions(X)
        ps.frame_tick()

import os

import numpy as np
import polyscope as ps

import time


import polyscope.imgui as psim
class WeightsViewer():
    def __init__(self, V, F, W,

              path="",
              R=np.identity(3), period=0,
                 vminmax=None, P=None, s=None, l=None, alpha=1, interactive=True):

        write_png = False
        if (path != ""):
            write_png = True
            os.makedirs(path, exist_ok=True)

        ps.init()
        ps.remove_all_structures()

        self.path = path
        if F.shape[1] == 1:
            self.mesh = ps.register_point_cloud("mesh", V @ R.T, color=[1, 0.1, 0.1], transparency=alpha)
        elif F.shape[1] == 2:
            self.mesh = ps.register_curve_network("mesh", V @ R.T, F, color=[1, 0.1, 0.1], transparency=alpha)
        elif F.shape[1] == 3:
            self.mesh = ps.register_surface_mesh("mesh", V @ R.T, F, color=[1, 0.1, 0.1], transparency=alpha)
        elif F.shape[1] == 4:
            self.mesh = ps.register_volume_mesh("mesh", V @ R.T, F, color=[1, 0.1, 0.1], transparency=alpha)
        self.W = W
        self.mesh.add_scalar_quantity("weights", np.zeros((V.shape[0])),  enabled=True, cmap='coolwarm')
        self.i = 0
        self.write_png = write_png
        self.period = period
        self.vminmax = vminmax
        self.max_frame = self.W.shape[1]
        self.interactive = interactive
        ps.reset_camera_to_home_view()
        self.id = 0
        if (P is not None):
            self.draw_bones = True
            self.P = P
            if s is None:
                s = 2
            if l is None:
                l = np.ones((W.shape[1]))
            self.s = s
            self.l = l
            alpha = 0.5
            self.mesh.set_transparency(alpha)


        ps.set_user_callback(self.anim)
        ps.show()

        # self.mesh.remove()



    def anim(self):
        if not self.interactive:
            if (self.i < self.max_frame):
                mesh = self.mesh
                i = self.i
                w = np.abs(self.W[:, i]).max()
                self.mesh.add_scalar_quantity("weights", self.W[:, i],  enabled=True, vminmax=[-w, w], cmap='coolwarm')
                # ps.set_camera_rotation(self.R)
                if (self.write_png):
                    ps.screenshot(self.path + "/" + str(i).zfill(4) + ".png", False)

                self.i += 1
                time.sleep(self.period)
        else:
            # print("interactive")
            # print(self.id)
            changed, ID = psim.SliderInt("bone ID", self.id, v_min=0, v_max=self.W.shape[1] - 1)
            if changed:
                self.id = ID

                w = np.abs(self.W[:, self.id]).max()
                self.mesh.add_scalar_quantity("weights", self.W[:, self.id], enabled=True,
                                              vminmax=[-w, w], cmap='coolwarm')


            return

        return
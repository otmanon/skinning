import numpy as np
from read_rig_from_json import read_rig_from_json
from read_rig_anim_from_json import read_rig_anim_from_json
from world2rel import world2rel
from rotate_rig import rotate_rig
def load_rig_anim(rig_file, rig_anim_file, rotate_to_y_up=True):
    X0, F, W, P0, lengths, pI = read_rig_from_json(rig_file)
    P = read_rig_anim_from_json(rig_anim_file)

    Prel = world2rel(P, P0)
    if rotate_to_y_up:
        # scipy
        from scipy.spatial.transform import Rotation as R
        rot = R.from_rotvec(np.array([-np.pi / 2, 0, 0])).as_matrix()
        Prel = rotate_rig(Prel, rot)

    return X0, F,W, Prel
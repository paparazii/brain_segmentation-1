__author__ = 'adeb'


data_path = "./data/"
file_path = data_path + "ultimate_test.h5"

general = {
    "source": "miccai",
    "source_folder": "2",
    "n_patch_per_voxel": 1,
    "file_path": file_path,
    "perm": False,
    "n_data": 10000
}

pick_vx = {
    "where": "anywhere",  # anywhere, plane
    "plane": 100,
    "axis": 1,
    "how": "random"  # all, random, balanced
}

pick_patch = {
    "how": "3D",  # 2Dortho, 2DorthoRotated, 3D
    "patch_width": 11,
    "axis": 1,
    "max_degree_rotation": 20
}

pick_tg = {
    "how": "center"  # center, proportion
}
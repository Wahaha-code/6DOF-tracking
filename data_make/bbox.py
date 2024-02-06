import numpy as np
import trimesh

mesh = trimesh.load('1.obj')
mesh.show()
to_origin, extents = trimesh.bounds.oriented_bounds(mesh)
bbox = np.stack([-extents/2, extents/2], axis=0).reshape(2,3)
__author__ = 'Robert Meyer'

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

from pypet.environment import Environment
from pypet.utils.explore import cartesian_product
from pypet import pypetconstants


def multiply(traj):
    """Sophisticated simulation of multiplication"""
    z=traj.x*traj.y
    traj.f_add_result('z',z, comment='I am the product of two reals!')


# Create an environment that handles running
env = Environment(trajectory='Example10',filename='experiments/example_08/HDF5/example_10.hdf5',
                  file_title='Example10', log_folder='experiments/example_08/LOGS/',
                  comment='Another example!')

# Get the trajectory from the environment
traj = env.v_trajectory

# Add both parameters
traj.f_add_parameter('x', 1, comment='I am the first dimension!')
traj.f_add_parameter('y', 1, comment='I am the second dimension!')

# Explore the parameters with a cartesian product:
x_length = 15
y_length = 15
traj.f_explore(cartesian_product({'x':range(x_length), 'y':range(y_length)}))

# Run the simulation
env.f_run(multiply)

# We load all results
traj.f_load(load_results=pypetconstants.LOAD_DATA)

# We access the ranges for plotting
xs = traj.f_get('x').f_get_range()
ys = traj.f_get('y').f_get_range()

# Now we want to directly get all numbers z from all runs
# for plotting.
# We use `fast_access=True` to directly get access to
# the values.
# Moreover, since `f_get_from_runs` returns an ordered dictionary
# `values()` gives us all values already in the correct order of the runs.
zs = traj.f_get_from_runs(name='z',fast_access=True).values()

# Convert the lists to numpy 2D arrays
x_mesh = np.reshape(np.array(xs),(x_length, y_length))
y_mesh = np.reshape(np.array(ys),(x_length, y_length))
z_mesh = np.reshape(np.array(zs),(x_length, y_length))

# Make fancy 3D plot
fig=plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x_mesh, y_mesh, z_mesh, rstride=1, cstride=1)
plt.show()
import numpy as np

def takens(data):
    return np.array([[data[i], data[i+1], data[i + 2]] for i in range(len(data) - 2)])

def velocity(coordinates):
    x = np.array(coordinates[:, 0])
    y = np.array(coordinates[:, 1])
    z = np.array(coordinates[:, 2])
    return np.array([ - x - 2*x*z**2, -y - 2*y*z**2, -z - 2*x**2*z - 2*y**2*z - z**2])

def energy(x, y, z):
    return np.array([0.5*(x[i]**2 + z[i]**2 + y[i]**2) + (x[i]**2 + y[i]**2)*z[i] + 1/3*z[i]**3 for i in range(len(x))])

def hamilton(velocity, energy):
    px = np.array(velocity[0])
    py = np.array(velocity[1])
    pz = np.array(velocity[2])
    return np.array(0.5*(px**2 + py**2 + pz**2) + energy)

def starting_points(hamilton, coordinates, velocity, h):
    condition = []
    for point in range(len(hamilton)):
        if hamilton[point] < h:
            condition += [np.array([0, velocity[0][point],
                                   coordinates[:, 1][point],velocity[1][point],
                                   coordinates[:, 2][point],velocity[2][point]])]
    return condition

def func(y, x):
    # return [x, px, y, py, z, pz]
    return np.array([y[1], -y[0] - 2*y[0]*y[4]**2, 
                    y[3], - y[2] - 2*y[2]*y[4]**2, 
                    y[5], - y[4] - 2*y[0]**2*y[4] - 2*y[2]**2*y[4] - y[4]**2])

def crossing(x, y, py):
    croos_y = []
    croos_py = []
    for i in range(len(x) - 1):
        if x[i] < 0 and x[i+1] > 0:
            croos_y += [(y[i] + y[i+1])/2]
            croos_py += [(py[i] + py[i+1])/2]
        elif x[i] > 0 and x[i+1] < 0:
            croos_y += [(y[i] + y[i+1])/2]
            croos_py += [(py[i] + py[i+1])/2]
    return croos_y, croos_py

def equipotential(energy, vectors, target):
    equipotential = []
    for i in range(len(energy)):
        if target == round(energy[i], 2):
            equipotential += [vectors[i]]
    return np.array(equipotential)
import numpy as np

def takens(data):
    return np.array([[data[i], data[i+1]] for i in range(len(data) - 1)])

def velocity(coordinates):
    x = np.array(coordinates[:,0])
    y = np.array(coordinates[:,1])
    return np.array([-x - 2*x*y, -y - x**2 + y**2])

def energy(x, y):
    return [0.5*(x[i]**2 + y[i]**2) + x[i]**2*y[i] - 1/3*y[i]**3 for i in range(len(x))]

def hamilton(velocity, energy):
    return np.array([0.5*(velocity[0][i]**2 + velocity[1][i]**2) + energy[i] for i in range(len(energy))])

def starting_points(hamilton, coordinates, velocity, e):
    condition = []
    for point in range(len(hamilton)):
        if hamilton[point] < e:
            condition += [np.array([0, velocity[0][point], coordinates[:,1][point],   velocity[1][point]])]
    return condition

def func(y,x):
    return np.array([y[1], -y[0] - 2*y[0]*y[2], y[3], -y[2] - y[0]**2 + y[2]**2])

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
        if target == round(energy[i],2):
            equipotential += [vectors[i]]
    return np.array(equipotential)


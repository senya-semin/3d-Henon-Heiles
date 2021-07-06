import numpy as np
from numpy.core.fromnumeric import take
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def takens(data):
    return np.array([[data[i], data[i+1]] for i in range(len(data) - 1)])

def velocity(coordinates):
    x = np.array(coordinates[:,0])
    y = np.array(coordinates[:,1])
    return np.array([-x - 2*x*y, -y - x**2 + y**2])

def hamilton(coordinates, velocity):
    return np.array([0.5*(velocity[0][i]**2 + velocity[1][i]**2 + coordinates[:,0][i]**2 + coordinates[:,1][i]**2) + coordinates[:,0][i]**2*coordinates[:,1][i] - coordinates[:,1][i]**3/3 for i in range(len(coordinates))])

def starting_points(hamilton, coordinates, velocity, e):
    condition = []
    for point in range(len(hamilton)):
        if hamilton[point] < e:
            condition += [np.array([0, velocity[0][point], coordinates[:,1][point],   velocity[1][point]])]
    return condition

def func(y,x):
    return np.array([y[1], -y[0] - 2*y[0]*y[2], y[3], -y[2] - y[0]**2 + y[2]**2])

def rungekutta4(f, y0, t):  
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    h = t[1] - t[0]
    for i in range(n - 1):
        k1 = f(y[i], t[i])[0]
        k2 = f(y[i] + k1 * h / 2, t[i] + h / 2)[0]
        k3 = f(y[i] + k2 * h / 2, t[i] + h / 2)[0]
        k4 = f(y[i] + k3 * h, t[i] + h)[0]
        y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
    return y


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
        if target[0] == round(energy[i],2) < target[0]:
            equipotential += [vectors[i]]
    return np.array(equipotential)

def equipotential_(energy, vectors, target):
    equipotential = []
    for i in range(len(energy)):
        if target == round(energy[i],2):
            equipotential += [vectors[i]]
    return np.array(equipotential)

def energy(x, y):
    return [0.5*(x[i]**2 + y[i]**2) + x[i]**2*y[i] - 1/3*y[i]**3 for i in range(len(x))]

#data = [np.sin(i) + np.random.random() for i in range(1000)]
#data = [np.sin(i) + np.cumsum(np.random.randint(-50, 50, 1000)/100)[i] for i in range(1000)]
data = np.random.randint(-200,200,10000)/100
#sns.lineplot(x=range(data.size), y = data)
takens = takens(data)
#print(takens)
velocity = velocity(takens)
hamilton = hamilton(takens, velocity)
conditions = starting_points(hamilton, takens, velocity, 1/12)
t = np.arange(0,1000,0.01)
#way = [rungekutta4(func, condition, t) for condition in conditions]
attractors = [odeint(func, condition, t) for condition in conditions]
fig, ax = plt.subplots(figsize=(10, 5), dpi=80)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
energys = energy(takens[:,0], takens[:,1])
target = [3,2,1,0.5,0.17,0.1,0.05]
equipotentials = [equipotential_(energys, takens, target[i]) for i in range(len(target))]
print(equipotentials)
for i in equipotentials:
    #if len(i) > 1:
    sns.scatterplot(x = i[:,0], y = i[:,1])
        #i = np.sort(i)
        #plt.contour(i)
#for attractor in attractors:
    #y, py = crossing(attractor[:,0], attractor[:,2], attractor[:,3])
    #sns.scatterplot(x = y, y = py)
    #x = attractor[:,0]
    #y = attractor[:,2]
    #z = attractor[:,3]
    #ax.plot(x,y,z)
    #plt.plot(attractor[:,0], attractor[:,2])


plt.show()
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import henon_heiles_3d as hh

data = [np.sin(i) + np.random.randint(-1, 1) for i in range(1000)]

takens = hh.takens(data)
velocity = hh.velocity(takens)
takens = hh.takens(data)
velocity = hh.velocity(takens)
energy = hh.energy(takens[:, 0], takens[:, 1], takens[:,2])
hamilton = hh.hamilton(velocity, energy)
conditions = hh.starting_points(hamilton, takens, velocity, 1/12)

a = 0.01
size = 750
t = np.arange(0,size,a)
integrals = [odeint(hh.func, condition, t) for condition in conditions]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = takens[:,0]
y = takens[:,1]
z = takens[:,2]
ax.set_xlabel('$y$')
ax.set_ylabel('$y + 1$')
ax.set_zlabel('$y + 2$')
plt.title("takens 3d")
ax.plot(x,y,z)
plt.show()
plt.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for integral in integrals:
    x = integral[:,1]
    y = integral[:,0]
    z = integral[:,5]
    ax.plot(x,y,z)
    break
ax.set_xlabel('$px$')
ax.set_ylabel('$x$')
ax.set_zlabel('$pz$')
plt.show()
plt.clf()

for integral in integrals:
    y, py = hh.crossing(integral[:,2], integral[:,1], integral[:,4])
    sns.scatterplot(x = y, y = py)
    #break
plt.xlabel("y")
plt.ylabel("py")
plt.show()
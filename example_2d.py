import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import henon_heiles_2d as hh

data = [np.sin(i) + np.random.randint(-1, 1) for i in range(1000)]

takens = hh.takens(data)
velocity = hh.velocity(takens)
energy = hh.energy(takens[:, 0], takens[:, 1])
hamilton = hh.hamilton(velocity, energy)
conditions = hh.starting_points(hamilton, takens, velocity, 1/12)

a = 0.01
size = 1000
t = np.arange(0,size,a)
integrals = [odeint(hh.func, condition, t) for condition in conditions]

fig, ax = plt.subplots(figsize=(10, 5), dpi=80)

#plotting original data
sns.lineplot(x = range(len(data)), y = data)
plt.xlabel("x")
plt.ylabel("y")
plt.title("data")
plt.savefig("data.png")
plt.clf()

#plotting takens theorem
plt.plot(takens[:,0], takens[:,1])
plt.xlabel("y")
plt.ylabel("y + 1")
plt.title("takens")
plt.savefig("takens.png")
plt.clf()

#plotting y vs. py
for integral in integrals:
    y, py = hh.crossing(integral[:,0], integral[:,2], integral[:,3])
    sns.scatterplot(x = y, y = py)
plt.xlabel("y")
plt.ylabel("py")
plt.savefig("y_py.png")
plt.clf()

#ploting x vs. y
for integral in integrals:
    plt.plot(integral[:,0], integral[:,1])
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("x_y.png")
plt.clf()

#plotting x vs. y vs. py
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for integral in integrals:
    x = integral[:,0]
    y = integral[:,2]
    z = integral[:,3]
    ax.plot(x,y,z)
    plt.plot(integral[:,0], integral[:,2])
plt.savefig("3d.png")
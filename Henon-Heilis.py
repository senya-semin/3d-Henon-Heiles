import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import functions

cumulat = np.cumsum(np.random.randint(-50, 50, 1000)/100)
data = [np.sin(i) + cumulat[i] for i in range(1000)]


takens = functions.takens(data)
velocity = functions.velocity(takens)
energy = functions.energy(takens[:, 0], takens[:, 1])
hamilton = functions.hamilton(velocity, energy)
conditions = functions.starting_points(hamilton, takens, velocity, 1/12)
t = np.arange(0,1000,0.01)
integrals = [odeint(functions.func, condition, t) for condition in conditions]

fig, ax = plt.subplots(figsize=(10, 5), dpi=80)
for integral in integrals:
    y, py = functions.crossing(integral[:,0], integral[:,2], integral[:,3])
    sns.scatterplot(x = y, y = py)
plt.xlabel("y")
plt.ylabel("py")
plt.savefig("scatters.png")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for integral in integrals:
    x = integral[:,0]
    y = integral[:,2]
    z = integral[:,3]
    ax.plot(x,y,z)
    plt.plot(integral[:,0], integral[:,2])
plt.savefig("3d.png")
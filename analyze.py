
from matplotlib import pyplot as plt
import numpy as np

data_back = np.load("data/back_leg_sensor.npy")
data_front = np.load("data/front_leg_sensor.npy")

plt.figure()
plt.plot(data_back, label = "Back Leg")
plt.plot(data_front, label = "Front Leg")
plt.xlabel("step")
plt.ylabel("value")
plt.legend()
plt.show()
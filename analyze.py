
from matplotlib import pyplot as plt
import numpy as np

data_back = np.load("data/back_leg_sensor.npy")
data_front = np.load("data/front_leg_sensor.npy")
data_sin = np.load("data/sin_wave")

plt.figure(1)
#plt.plot(data_back, label = "Back Leg")
#plt.plot(data_front, label = "Front Leg")
#plt.xlabel("step")
#plt.ylabel("value")
plt.plot(data_sin)
plt.show()
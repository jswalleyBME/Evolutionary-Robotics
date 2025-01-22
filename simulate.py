
# evolutionary robotics HW1
import pybullet as p
import time

physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

count = 0
for _ in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    count+=1
    print(count)

p.disconnect()

# evolutionary robotics HW1
import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())  # location of .urdf
p.setGravity(0,0,-9.8)                                  # gravity
planeId = p.loadURDF("plane.urdf")                      # set floor 
p.loadSDF("box.sdf")                                    

count = 0
for _ in range(1000):
    
    # step simulation and time delay 
    p.stepSimulation()
    time.sleep(1/60)
    count+=1
    print(count)

p.disconnect()
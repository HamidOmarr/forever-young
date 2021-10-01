from RobotArm import RobotArm
robotArm = RobotArm('exercise 4')

for A in range (3):
    robotArm.grab()
    for A in range (2):
      robotArm.moveRight()
    robotArm.drop()
    for A in range (2):
        robotArm.moveLeft()

for A in range (2):
    robotArm.moveRight()
    
for A in range (3):
    robotArm.grab()
    for A in range (1):
      robotArm.moveLeft()
    robotArm.drop()
    for A in range (1):
        robotArm.moveRight()
robotArm.wait()
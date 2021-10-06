from RobotArm import RobotArm
robotArm = RobotArm('exercise 6')

for A in range (7):
    robotArm.moveRight()

robotArm.grab()     
robotArm.moveRight()
robotArm.drop()

for A in range (7):
    for A in range (2):
        robotArm.moveLeft()
    robotArm.grab()
    for A in range (1):
        robotArm.moveRight()
    robotArm.drop()

robotArm.wait() 
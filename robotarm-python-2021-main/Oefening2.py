from RobotArm import RobotArm
robotArm = RobotArm('exercise 2')
robotArm.grab()
for A in range (9):
    robotArm.moveRight()
robotArm.drop()
for B in range (5):
    robotArm.moveLeft()
robotArm.grab()
for C in range (5):
    robotArm.moveRight()
robotArm.drop()
for C in range (2):
    robotArm.moveLeft()
robotArm.grab()
for C in range (2):
    robotArm.moveRight()
robotArm.drop()
robotArm.wait()
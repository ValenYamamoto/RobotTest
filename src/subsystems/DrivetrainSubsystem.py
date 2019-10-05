'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
import subsystems.Subsystem as Subsystem
import externals.Motor as Motor

class DrivetrainSubsystem(Subsystem):
    def __init__(self):
        self.name = "DrivetrainSubsystem"
        self.motorLeft = Motor(0)
        self.motorRight = Motor(1)
    
    def setRawPower(self, rightPower, leftPower):
        self.motorLeft.set(leftPower)
        self.motorRight.set(rightPower)
        
    def driveFwdRot(self, fwd, rot):
        right = fwd - rot
        left = fwd + rot
        
        max = max(abs(right), abs(left), 1)
        
        right /= max
        left /= max
        
        self.setRawPower(right, left)
              
    def commandConflict(self, commands):
        firstCommand = commands[0]
        for command in commands:
            if(command.getInitTime() < firstCommand.getInitTime()):
                firstCommand = command
        return firstCommand
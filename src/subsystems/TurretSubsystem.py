'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
import externals.Motor as Motor
import subsystems.Subsystem as Subsystem

class TurretSubsystem(Subsystem):
    
    def __init__(self):
        self.name = "TurretSubsystem"
        self.turretMotor = Motor(3)
        
    def setPower(self, power):
        self.turretMotor.set(power)
        
    def commandConflict(self, commands):
        firstCommand = commands[0]
        for command in commands:
            if(command.getInitTime() < firstCommand.getInitTime()):
                firstCommand = command
        return firstCommand
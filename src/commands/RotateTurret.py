'''
Created on Oct 7, 2019

@author: Valen Yamamoto
'''
import commands.Command as Command
from subsystems.TurretSubsystem import turret

class RotateTurret(Command):
    
    def __init__(self, power):
        super()
        
        self.requires(turret)
        
        self.name = "Turret Command" + str(id(self))
        self.power = power
        
    def setUp(self):
        if(self.isInitialized):
            turret.set_power(self.power)
        self.isSetUp = True
    
    def Execute(self):
        if(self.isSetUp):
            self.isExecuting = True
            if(self.isFinished()):
                print("Finished")
                self.isExecuting = False
        
    def isFinished(self):
        return True
    
    def end(self):
        return
    
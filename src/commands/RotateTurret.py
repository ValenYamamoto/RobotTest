'''
Created on Oct 7, 2019

@author: Valen Yamamoto
'''
from commands.Command import Command
from subsystems.TurretSubsystem import turret
import time

class RotateTurret(Command):
    
    def __init__(self, power):
        super()
        
        self.requires(turret)
        
        self.name = "TurretCommand" + str(id(self))
        self.power = power
        self.is_initialized = True
        self.is_set_up = False
        self.is_executing = False
        self.finished = False
        self.init_time = time.time()
        
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
    
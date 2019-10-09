'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
from commands.Command import Command
from subsystems.DrivetrainSubsystem import drivetrain
import time

class DriveForwardRotate(Command):
    
    def __init__(self, fwd, rot):
        super()
        self.requires(drivetrain)
        
        self.name = "DriveCommand" + str(id(self))
        self.fwd = fwd
        self.rot = rot
        self.is_initialized = True
        self.is_set_up = False
        self.is_executing = False
        self.finished = False
        self.init_time = time.time()
        
    def setUp(self):
        if(self.isInitialized):
            drivetrain.drive_fwd_rot(self.fwd, self.rot)
        self.isSetUp = True
    
    def Execute(self):
        if(self.is_set_up):
            self.is_executing = True
            if(self.is_finished()):
                print("Here")
                self.is_executing = False
        
    def isFinished(self):
        return True
    
    def end(self):
        return
    
    def toString(self):
        return self.name
    

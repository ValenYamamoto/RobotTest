'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
import commands.Command as Command
import robot.Robot as Robot

class DriveForwardRotate(Command):
    
    def __init__(self, fwd, rot):
        super()
        
        self.requires(Robot.Robot.drivetrain)
        
        self.name = "DriveCommand" + str(id(self))
        self.fwd = fwd
        self.rot = rot
        
    def setUp(self):
        if(self.isInitialized):
            Robot.Robot.drivetrain.driveFwdRot(Robot.Robot.drivetrain, fwd, rot)
        self.isSetUp = True
    
    def Execute(self):
        if(self.isSetUp):
            self.isExecuting = True
            if(self.isFinished()):
                break
        self.isExecuting = False
        
    def isFinished(self):
        return True
    
    def end(self):
        return
    

'''
Created on Oct 11, 2019

@author: Valen Yamamoto
'''
from commands.Command import Command
from subsystems.DrivetrainSubsystem import drivetrain
from algorithms.PID import PID
import time

class DrivetrainPID(Command):
    
    def __init__(self, setpoint):
        super()
        
        self.requires(drivetrain)
        
        self.name = "DrivetrainPIDCommand" + str(id(self))
        
        self.setpoint = setpoint
        self.is_initialized = True
        self.is_set_up = False
        self.is_executing = False
        self.finished = False
        self.init_time = time.time()
        
        self.pid_controller = PID(drivetrain.DrivetrainPIDConstants.k_p,
                                  drivetrain.DrivetrainPIDConstants.k_i,
                                  drivetrain.DrivetrainPIDConstants.k_d,
                                  name = 'DrivetrainPID' + str(id(self)))
        
    def setUp(self):
        if(self.is_initialized):
            self.pid_controller.PID_setup(self.setpoint)
        self.is_set_up = True
    
    def Execute(self):
        if(self.is_set_up):
            self.is_executing = True
            output = self.pid_controller.get_PID_output(0)
            drivetrain.set_raw_power(output, output)
            if(self.is_finished()):
                print("Finished")
                self.isExecuting = False
        
    def is_finished(self):
        return self.pid_controller.is_within_tolerance(0)
    
    def end(self):
        return
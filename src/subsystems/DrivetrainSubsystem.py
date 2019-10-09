'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
from subsystems.Subsystem import Subsystem
from externals.Motor import Motor

class DrivetrainSubsystem(Subsystem):
    
    def __init__(self):
        self.name = "DrivetrainSubsystem"
        self.motor_left = Motor(0)
        self.motor_right = Motor(1)
    
    def set_raw_power(self, right_power, left_power):
        self.motor_left.set(left_power)
        self.motor_right.set(right_power)
        
    def drive_fwd_rot(self, fwd, rot):
        right = fwd - rot
        left = fwd + rot
        
        max = max(abs(right), abs(left), 1)
        
        right /= max
        left /= max
        
        self.set_raw_power(right, left)
              
    def command_conflict(self, commands):
        print(commands)
        first_command = commands[0]
        for command in commands:
            if(command.get_init_time() < first_command.get_init_time()):
                first_command = command
        return first_command
    
    def toString(self):
        return self.name
    
drivetrain = DrivetrainSubsystem()
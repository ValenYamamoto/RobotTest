'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
from subsystems.Subsystem import Subsystem
from externals.Motor import Motor

class DrivetrainSubsystem(Subsystem):
    
    PID_command_name = "DrivetrainPIDCommand"
    
    class DrivetrainPIDConstants:
        k_p = 0
        k_i = 0
        k_d = 0
    
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
        
        maximum = max(abs(right), abs(left), 1)
        
        right /= maximum
        left /= maximum
        
        self.set_raw_power(right, left)
              
    def command_conflict(self, commands):
        print("In drivetrain command conflict")
        print(commands, end="\n\n")
        first_command = commands[0]
        names = self.get_names(commands)
        
        for name in names:
            print("Here: ", name)
            if(self.PID_command_name in name): 
                print("Command name match")
                for command in commands:
                    if(self.PID_command_name not in command.get_name()):
                        commands.remove(command)
                        break
                
        for command in commands:
            if(command.get_init_time() < first_command.get_init_time()):
                first_command = command
        return first_command
    
    def toString(self):
        return self.name
    
drivetrain = DrivetrainSubsystem()
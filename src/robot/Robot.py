'''
Created on Oct 3, 2019

@author: Valen Yamamoto
'''
import subsystems.DrivetrainSubsystem as DrivetrainSubsystem
import commands.CommandScheduler as CommandScheduler

class Robot:
    def __init__(self):
        self.drivetrain = DrivetrainSubsystem()
        self.scheduler = CommandScheduler()
        

robot = Robot()
'''
Created on Oct 8, 2019

@author: Valen Yamamoto
'''
from commands.Command import Command
from subsystems.TurretSubsystem import turret
from algorithms.PID import PID
import time

class TurretPID(Command):
    
    def __init__(self, setpoint):
        super()
        
        self.requires(turret)
        
        self.name = "TurretPIDCommand" + str(id(self))
        
        self.setpoint = setpoint
        self.is_initialized = True
        self.is_set_up = False
        self.is_executing = False
        self.finished = False
        self.init_time = time.time()
        
        self.pos = 0
        
        self.pid_controller = PID(turret.TurretPIDConstants.k_p,
                                  turret.TurretPIDConstants.k_i,
                                  turret.TurretPIDConstants.k_d,
                                  name = 'TurretPID' + str(id(self)))
        
    def set_up(self):
        if(self.is_initialized):
            self.pid_controller.PID_setup(self.setpoint)
            self.pid_controller.set_absolute_tolerance(1)
        self.is_set_up = True
    
    def execute(self):
        if(self.is_set_up):
            self.is_executing = True
            turret.set_power(self.pid_controller.get_PID_output(turret.get_position()))
            print("PID output:", self.pid_controller.get_PID_output(turret.get_position()))
            print("Turret Power:", turret.get_power())
            if(self.is_finished()):
                print("Finished")
                self.isExecuting = False
        
    def is_finished(self):
        print("IN IS FINISHED")
        return self.pid_controller.is_within_tolerance(turret.get_position())
    
    def end(self):
        return
    
if __name__ == "__main__":
    pid = TurretPID(90)
    turret.set_position(0)
    print("Current Position:", turret.get_position())
    pid.set_up()
    pid.execute()
    turret.set_position(45)
    print("Current Position:", turret.get_position())
    pid.execute()
    turret.set_position(90)
    print("Current Position:", turret.get_position())
    pid.execute()
    pid.execute()
    
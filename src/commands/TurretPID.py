'''
Created on Oct 8, 2019

@author: Valen Yamamoto
'''
from commands.Command import Command
from subsystems.TurretSubsystem import turret
from algorithms.PID import PID

class TurretPID(Command):
    
    def __init__(self, setpoint):
        super()
        
        self.requires(turret)
        
        self.name = "Turret PID Command" + str(id(self))
        self.setpoint = setpoint
        self.pid_controller = PID(turret.TurretPIDConstants.k_p,
                                  turret.TurretPIDConstants.k_i,
                                  turret.TurretPIDConstants.k_d,
                                  name = 'TurretPID' + str(id(self)))
        
    def setUp(self):
        if(self.is_initialized):
            self.pid_controller.PID_setup(self.setpoint)
        self.is_set_up = True
    
    def Execute(self):
        if(self.is_set_up):
            self.is_executing = True
            turret.set_power(self.pid_controller.get_PID_output(0))
            if(self.is_finished()):
                print("Finished")
                self.isExecuting = False
        
    def is_finished(self):
        return self.pid_controller.is_within_tolerance(0)
    
    def end(self):
        return
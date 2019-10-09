'''
Created on Oct 7, 2019

@author: Valen Yamamoto
'''
class PID:
    
    def __init__(self, k_p, k_i, k_d, name = "PID"):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.is_absolute_tolerance = True
        self.name = name + str(id(self))
        
    def set_k_p(self, k_p):
        self.k_p = k_p
        
    def set_k_i(self, k_i):
        self.k_i = k_i
        
    def set_k_d(self, k_d):
        self.k_d = k_d
       
    def setPID(self, k_p, k_i, k_d):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d

    def set_setpoint(self, setpoint):
        self.setpoint = setpoint
        
    def set_absolute_tolerance(self, abs_tol):
        self.absolute_tolerance = abs_tol
        self.is_absolute_tolerance = True
        
    def set_percent_tolerance(self, percent_tol):
        self.percent_tolerance = percent_tol
        self.is_absolute_tolerance = False
        
    def get_k_p(self):
        return self.k_p
    
    def get_k_i(self):
        return self.k_i
    
    def get_k_d(self):
        return self.k_d
    
    def get_setpoint(self):
        return self.setpoint
        
    def PID_setup(self, setpoint):
        self.integral = 0
        self.last_val = 0
        self.setpoint = setpoint
        
        if(self.is_absolute_tolerance is True):
            self.tolerance = self.absolute_tolerance
        else:
            self.tolerance = self.percent_tolerance * self.setpoint
        self.is_finished = False
        
    def get_PID_output(self, current):
        error = self.get_setpoint() - current
        self.integral += error
        derivative = current - self.last_val
        self.last_val = current
        
        if(self.is_finished is True or self.is_within_tolerance(current) is True):
            return 0
        return self.k_p * error + self.k_i * self.integral + self.k_d * derivative
        
    def is_within_tolerance(self, current):
        if(abs(current - self.setpoint) < self.tolerance):
            return True
        return False
        
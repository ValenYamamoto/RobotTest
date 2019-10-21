'''
Created on Oct 16, 2019

@author: Valen Yamamoto
'''
import numpy as np
class Spline:
    
    def __init__(self, points):
        self.points = points
        
    def get_hi(self, i):
        return self.points[i+1].get_x() - self.points[i].get_x()
    
    def get_bi(self, i):
        return (1/self.get_hi(i)) * (self.points[i+1].get_y() - self.points[i].get_y())
    
    def get_vi(self, i):
        return 2 * (self.get_hi(i-1) + self.get_hi(i))
    
    def get_ui(self, i):
        return 6 * (self.get_bi(i) - self.get_bi(i-1))
    
    def get_h_array(self):
        array = []
        
        for i in range(len(self.points) - 1):
            array.append(self.get_hi(i))
        return array
            
    def get_v_array(self):
        array = []
        
        for i in range(len(self.points) - 3):
            i += 1
            array.append(self.get_vi(i))
        return array
    
    def get_u_array(self):
        array = []
        
        for i in range(len(self.points) - 3):
            i += 1
            array.append(self.get_ui(i))
        return array
    
    def get_tridiag_matrix(self):
        pass
    
    def get_gamma_array(self):
        h_array = self.get_h_array()
        v_array = self.get_v_array()
        
        array = []
        array.appned(h_array[0] / v_array[0])
        
        for i in range(len(self.points) - 1):
            i += 1
            array.append(h_array(i) / (v_array(i) - h_array(i - 1) * array[i-1]))
        
        return array
    
    def get_rho_array(self):
        h_array = self.get_h_array()
        v_array = self.get_v_array()
        u_array = self.get_u_array()
        gamma_array = self.get_gamma_array()
        
        array = []
        array.append(u_array[0] / v_array[0])
        
        for i in range(len(self.points) - 1):
            i += 1
            array.append((u_array[i] - h_array[i - 1] * array[i - 1]) / (h_array[i] - h_array[i - 1] * gamma_array[i - 1]))
            
        return array
    
    def get_z_array(self):
        rho_array = self.get_rho_array()
        h_array = self.get_h_array()
        u_array = self.get_u_array()
        v_array = self.get_v_array()
        gamma_array = self.get_gamma_array()
        
        array = []
        array.append(rho_array[-1])
        
        for i in range(len(self.points)):
            i += 2
            array.append((u_array[-i] - h_array[-i - 1] * rho_array[-i - 1])/ (v_array[-i] - h_array[-i - 1] * gamma_array[-i - 1]) * array[i - 1])
        
        return array
        
        
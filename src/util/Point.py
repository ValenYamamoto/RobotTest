'''
Created on Oct 14, 2019

@author: Valen Yamamoto
'''
import math
class Point:
    def __init__(self, x = 0, y = 0, heading = 0):
        self.x = x
        self.y = y
        self.heading = heading
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.x = y
        
    def get_heading(self):
        return self.heading
    
    def set_heading(self, heading):
        self.heading = heading
        
    def distance(self, point2):
        return math.sqrt((self.x - point2.get_x())**2 + (self.y - point2.get_y())**2)
    
    def heading_diff(self, point2):
        return point2.get_heading() - self.heading

    def __repr__(self):
        return "(%.2f, %.2f)" % (self.get_x(), self.get_y())
    
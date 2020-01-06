'''
Created on Oct 8, 2019

@author: Valen Yamamoto
'''
import math
from util.Point import Point
class PurePursuit():
    
    wheelbase = 1
    
    def __init__(self, x = 0, y = 0, heading=0, path=None):
        self.pos = Point(x, y)
        self.heading = 0
        
    def get_curvature(self, lookahead_point):
        a = math.tan(lookahead_point.get_heading())
        b = 1
        c = math.tan(lookahead_point.get_heading()) * self.pos.get_x() - self.pos.get_y()
        
        x = abs(a * lookahead_point.get_x() + b * lookahead_point.get_y() + c) / (math.sqrt(a * a + b * b))
        L = self.pos.distance(lookahead_point)
        
        side = math.sin(self.pos.get_heading()) * (lookahead_point.get_x() - lookahead_point.get_y()) - math.cos(lookahead_point.get_heading()) * (lookahead_point.get_y() - self.pos.get_y())
        
        return math.copysign(2*x/(L**2), side)
    
    def get_right_to_left_ratio(self, curv):
        return (2 + curv * self.wheelbase) / (2 - curv * self.wheelbase)
    
    
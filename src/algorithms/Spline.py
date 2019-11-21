'''
Created on Oct 16, 2019

@author: Valen Yamamoto
'''
import numpy as np
import matplotlib.pyplot as plot
from util.Point import Point
from cmath import sqrt
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
        
        for i in range(len(self.points) - 2):
            i += 1
            array.append(self.get_vi(i))
        return array
    
    def get_u_array(self):
        array = []
        
        for i in range(len(self.points) - 2):
            i += 1
            array.append(self.get_ui(i))
        return array
    

    def get_gamma_array(self):
        h_array = self.get_h_array()
        v_array = self.get_v_array()
        
        array = []
        array.append(h_array[0] / v_array[0])
        
        for i in range(len(self.points) - 2):
            i += 1
#             print(i, len(h_array), len(v_array), len(array))
            h_array[i]
            h_array[i - 1]
            array[i - 1]
            array.append(h_array[i] / (v_array[i - 1] - h_array[i - 1] * array[i - 1]))
        
        return array
    
    def get_rho_array(self):
        h_array = self.get_h_array()
        v_array = self.get_v_array()
        u_array = self.get_u_array()
        gamma_array = self.get_gamma_array()
        
        array = []
        array.append(u_array[0] / v_array[0])
        
        for i in range(len(self.points) - 2):
            i += 1
#             print(i, len(h_array), len(v_array), len(u_array), len(gamma_array))
            array.append((u_array[i - 1] - h_array[i - 1] * array[i - 1]) / (self.get_bi(i) - h_array[i - 1] * gamma_array[i - 1]))
#             print("u[i-1]", u_array[i-1])
#             print("h[i-1]", h_array[i-1])
#             print("array[i-1]", array[i-1])
#             print("b[i]", self.get_bi(i))
#             print("gamma[i-1]", gamma_array[i-1])
#             print(u_array[i - 1] - h_array[i - 1] * array[i - 1])
#             print(h_array[i] - h_array[i - 1] * gamma_array[i - 1])
#             print()
            
        return array
    
    def get_z_array(self):
        rho_array = self.get_rho_array()
        h_array = self.get_h_array()
        u_array = self.get_u_array()
        v_array = self.get_v_array()
        gamma_array = self.get_gamma_array()
        
        array = []
#         array.append(rho_array[-1])
        array.append(u_array[-1]/v_array[-1])
        
        for i in range(len(self.points) - 2):
            i += 2
            array.append((u_array[-i + 1] - h_array[-i] * array[i - 2]) / v_array[-i + 1])
#             array.append((u_array[-i + 1] - h_array[-i] * rho_array[-i])/ (v_array[-i + 1] - h_array[-i] * gamma_array[-i]) * array[i - 2])
        
#         return [0] + array
        return [0] + array[::-1]
    
    def get_si_array(self):
        z_array = self.get_z_array()
        h_array = self.get_h_array()
        
        a = []
        b = []
        c = []
        d = []
        
        for i in range(len(z_array) - 1):
#             print(i)
            a.append(z_array[i+1]/ (6 * h_array[i]))
            b.append(z_array[i] / (6 * h_array[i]))
#             b.append(0)
            c.append(points[i + 1].get_y()/h_array[i] - z_array[i + 1] * h_array[i]/6)
            d.append(points[i].get_y()/h_array[i] - h_array[i] * z_array[i] / 6)
            
        return a, b, c, d
        
    def generate_spline(self, step):
        co = self.get_si_array()
        
        x = points[0].get_x()
        x_array = []
        y_array = []
        
        
        for i in range(1, len(points)):
            x = points[i-1].get_x()
            self.print_formula(points[i-1], points[i], co[0][i-1], co[1][i-1], co[2][i-1], co[3][i-1] )
            while x <= points[i].get_x():
                x_array.append(x)
                y = co[0][i-1] * ((x - points[i-1].get_x()) ** 3) + co[1][i-1] * ((points[i].get_x() - x) ** 3) + \
                co[2][i-1] * (x - points[i-1].get_x()) + co[3][i-1] * (points[i].get_x() - x)
                y_array.append(y)
                x += step
        return x_array, y_array
    
    def print_formula(self, point, n, a, b, c, d):
        print("S(x) = %.2f(x - %.2f)^3 + %.2f(%.2f - x)^3 + %.2f(x- %.2f) + %.2f(%.2f - x)" % (a, point.get_x(), b, n.get_x(), c, point.get_x(), d, n.get_x()))
        
if __name__ == "__main__":
    points = []
    def get_cubic_curvature(x):
        num = abs(6 * x)
        den = abs(1 + (3 * x ** 2))
        den = den ** 3 
        den = den ** 0.5
        return num / den
    
    for x in range(-5, 6):
        points.append(Point(x, x ** 3, get_cubic_curvature(x)))
    print(points)
#     x = list(range(-5, 6))
#     y = [i ** 3 for i in x]
#     curv = [get_cubic_curvature(i) for i in x]
#     plot.subplot(2, 1, 1)
#     plot.plot(x, y)
#     plot.subplot(2, 1, 2)
#     plot.plot(x, curv)
#     plot.show()
    
    points = [Point(0.9, 1.3), Point(1.3,1.5), Point(1.9, 1.85), Point(2.1,2.1)]
    spline = Spline(points)
    
    print("h array", spline.get_h_array())
    print("v array", spline.get_v_array())
    print("u array", spline.get_u_array())
    print("gamma array", spline.get_gamma_array())
    print("rho array", spline.get_rho_array())
    print("z array", spline.get_z_array())
    
    x = [0.9, 1.3, 1.9, 2.1]
    y = [1.3, 1.5, 1.85, 2.1]
    plot.subplot(2,1,1)
    plot.plot(x, y)

    print(spline.get_si_array())
    print(spline.generate_spline(0.1))
    x, y = spline.generate_spline(0.1)
    
    plot.subplot(2,1,2)
    plot.plot(x,y)
    plot.show()
    
    points = [Point(-1, -1), Point(0, -5), Point(1, 1)]
    spline = Spline(points)
    
    print("h array", spline.get_h_array())
    print("v array", spline.get_v_array())
    print("u array", spline.get_u_array())
    print("gamma array", spline.get_gamma_array())
    print("rho array", spline.get_rho_array())
    print("z array", spline.get_z_array())
    
    x = [-1, 0, 1]
    y = [-1, -5, 1]
    plot.subplot(2,1,1)
    plot.plot(x, y)

    print(spline.get_si_array())
    print(spline.generate_spline(0.1))
    x, y = spline.generate_spline(0.1)
    
    plot.subplot(2,1,2)
    plot.plot(x,y)
    plot.show()
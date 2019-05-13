'''
Created on May 13, 2019

@author: jmullen19
'''


class Car:
    def __init__(self,c,m=0,s=0):
        self.color = c
        self.speed = s
        self.mileage = m
    
    def get_color(self):
        return self.color
    
    def get_speed(self):
        return  self.speed
    
    def get_milage(self):
        return self.mileage
    
def main():
    car1 = Car("red", 50000, 0)
    car2 = Car("black")
    car3 = Car("blue", 10)
    print(car1.get_color(), car1.get_speed(), car1.get_mileage())
    print(car2.get_color())
    
main()
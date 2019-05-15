'''
Created on May 15, 2019

@author: jmullen19
'''
class Car:
    def __init__(self,c,m=0,s=5,p=1,moc=0):
        self.color = c
        self.mileage = m
        self.num_seats = s
        self.passengers = p
        self.miles_since_oil_change = moc
        
        
    def get_color(self):
        return self.color
    
    def get_mileage(self):
        return self.mileage
    
    def get_num_seats(self):
        return self.num_seats
    
    def get_passengers(self):
        return self.passengers
    
    def get_miles_since_oil_change(self):
        return self.miles_since_oil_change
        
    def drive(self,miles):
        self.mileage  += miles
        self.miles_since_oil_change += miles

    def ready_for_oil_change(self):
        if self.mile_since_oil_change >= 3000: 
            return True
        else:
            return False
    
    def add_passengers(self,num_passengers):
        if num_passengers + self.passengers <= self.num_seats:
            self.passengers += num_passengers
            return True
        else:
            return False
    
    def change_oil(self):
        self.miles_since_oil_change = 0

def main():
    car1 = Car("red")
    car2 = Car("black",25)
    car3 = Car("blue",0,5,2)
    car1.drive(300)
    car2.add_passengers(3)
  

main()
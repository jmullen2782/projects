'''
Created on May 17, 2019
Yahtzee
@author: Jennie Mullen
'''
class Die:
    def __init__(self,v=0):
        self.__value = v
        
    def get_value(self):
        return self.__value
    
    def roll(self):
        import random
        self.__value = random.randint(1,6)  
    
class Yahtzee:
    dice_and_value = {}
    
    def look_value(self):
        return self.value
    
    def score(self):
        return self.score
def main():
    d1 = Die()
    d1.roll()
    print(d1.get_value())
main()
        
import click

class Greeting:
    
    def __init__(self):
        self.count = 1
   
    def welcome(self, name, count):
        
        for x in range(self.count):
            
            print("Welcome, {}".format(name))
        
    def menu(self, food):
        
        print("My favourite food is {}".format(food))

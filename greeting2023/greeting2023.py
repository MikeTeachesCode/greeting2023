import click

class Greeting(object):
    
    __author__ = 'Michael S. Russell'
    __email__ = 'miketeachingcode@yahoo.com'
    __version__ = '1.0.1'
    
    def __init__(self, count = 1):
        self.count = count
   
    def welcome(self, name):
        
        for x in range(self.count):
            
            print("Welcome, {}".format(name))
        
    def menu(self, food):
        
        print("My favourite food is {}".format(food))

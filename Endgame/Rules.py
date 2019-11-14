'''
Created on Oct 30, 2019

@author: sauga, wadood, and mashfik
'''

class Rules:
    
   def Reader(self): 
    #open the Rules txt file
    f = open("Rules.txt","R" )
    if f.mode == "R":
        #use the read() function to read the class
        f1 = f.readlines()
        for x in f1:
            print()
            
    # Create an empty Rules object        
    def __init__(self):
     self.rules = [] 
             
        

            
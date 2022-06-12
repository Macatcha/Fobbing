#!/usr/bin/env python3

# Purpose: Calculate the desired freshwater exchange (gal) needed to establish a viable calcium concentration level in pool
 
# Author: Macatcha
 
import sys 
import math

def pool_info():
	
  a = float(input("What is your current pool calcium concentration?(ppm)"))
	b = float(input("What is the calcium concentration of the water source?(ppm)"))
	c = float(input("What is the desired pool calcium concentration?(ppm)"))
	d = float(input("What is your pool capacity?(gal)"))
	
  return pool_info(a,b,c,d)

def calc_gal('a','b','c','d'):
        
        calc_gal = [((c-a)*d)/(b-a)]
        
        print("The total water to drain and refill with fresh water (gal) is", x)

             answer=input("Do you wish to exit program? (yes or no)")

             if answer == "yes":
                exit()

             else:
                print("Please rerun program")
    
pool_info()

calc_gal()

        

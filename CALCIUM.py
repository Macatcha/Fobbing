#!/usr/bin/env python3

# Purpose: Calculate the desired freshwater exchange (gal) needed to establish a viable calcium concentration level in pool
 
# Author: Macatcha
 
def pool_info():
        a = float(input("What is your current pool calcium concentration?(ppm)"))
        b = float(input("What is the calcium concentration of the water source?(ppm)"))
        c = float(input("What is the desired pool calcium concentration?(ppm)"))
        d = float(input("What is your pool capacity?(gallons or liters)"))
        system = input("Is your capacity in customary or metric systems?").lower().strip()
        return (a,b,c,d,system)
def calculate_vol(a,b,c,d,system):
        if system == 'customary':
                vol = ((c-a)*d)/(b-a)
        else:
                vol = ((c-a)*d)/(b-a)         
        return vol
while True:
        a, b, c, d, system = pool_info()
        if system.startswith('c'):
                vol = calculate_vol(a, b, c, d, system ='customary')
                print(f"Your volume to exchange is {vol} gallons")
                break
        elif system.startswith('m'):
                vol = calculate_vol(a, b, c, d)
                print(f"Your volume is {vol} liters")
		break
        else:
                print("An input error may have occurred. Try checking inputs and run again.")

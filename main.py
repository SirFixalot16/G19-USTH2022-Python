from pyparsing import nullDebugAction
from domains import *
from combine import *
import string

###
# Planes
###
p1 = Plane('Boeing 757', 'VN457')
p2 = Plane('Boeing 347', 'VN522')
p3, p4, p5, p6, p7, p8

###
# Flights
###
f1 = Flight('VN457', 0, 0, p1, 16, 20, 'Hanoi, Vietnam', 'Phu Quoc, Vietnam')
f2, f3, f4, f5

def main():
    print('Main')
    

if __name__ == "__main__":
    main()
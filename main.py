from domains.Flight import *
from domains.Plane import *
<<<<<<< HEAD
=======
from domains.Passenger import *
from GUI.manage import *
>>>>>>> cb54496ee53b70e9a0c3cecbf49a62723c6435e9

###
# Planes
###
p1 = Plane("Boeing 757", "VN457")
p2 = Plane("Boeing 347", "VN522")
# p3, p4, p5, p6, p7, p8 to be added

###
# Flights
###
f1 = Flight('VN457', 0, 0, 'Boeing 757', 16, 20, 'Hanoi, Vietnam', 'Phu Quoc, Vietnam')
# f2, f3, f4, f5 to be added

def main():
    print('Main')

if __name__ == "__main__":
    main()
    menu()
import string
import pickle
import random
from os import path

class Passenger:
    def __init__(self, name, pid, f_code, seat):
        self.name = string(name) 
        # Name; e.g.: Vu Quoc Thai
        self.pid = string(pid) 
        # Personal ID; e.g.: 001202001264

        self.f_code = string(f_code)
        # Flight code; e.g: VN457
        self.seat = string(seat)
        # Seat number; e.g.: 3F, 5A, 16B

    def validatePID(self, pid):
        if len(pid) < 13:
            return True
        else:
            return False
    # Validate function for personal ID, makes sure it follows Vietnam's ID

    def validateSeat(self, seat):
        tempstr = ''
        for x in range(0, len(string.ascii_uppercase)):
            temp = string.ascii_uppercase[x]
            if (seat[1] == temp) or (seat[2] == temp):
                tempstr = seat.replace(temp, '')
        if int(tempstr) in range(0, 20):
            return True
    # Validate function for seat, the first letter in range 1 to 20, and seat number from A to F

    def load_passenger_data(self, seat_booking):
        # load passenger data from pickle file
        with open('passenger_data', 'wb') as book:
            pickle.dump(seat_booking, book)

    def book_seat(self, seat_booking, booking_id):
        #func for booking seat
        if path.exists('passenger_data'):
            with open('passenger_data', 'rb') as seats:
                bseat = pickle.load(seats)
            if booking_id not in bseat:
                bseat.update(seat_booking)
            self.load_passenger_data(bseat)
        else:
            self.load_passenger_data(seat_booking)
    
    def get_infos(self, booking_id):
    #func to get ticket infos
        psg = dict()
        if path.exists('passenger_data'):
            with open('passenger_data', 'rb') as user_seat:
                psg = pickle.load(user_seat)
        if booking_id in psg:
            return psg[booking_id]
        else:
            print("Invalid Id..!")
            return {}
    

    ###
    # Setter and getters
    ###
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setPID(self, pid):
        self.pid = pid
    def getPID(self):
        return self.pid

    def setCode(self, code):
        self.f_code = code
    def getCode(self):
        return self.f_code
    def setSeat(self, seat):
        self.seat = seat
    def getSeat(self):
        return self.seat

        

class Plane:
    def __init__(self, name, f_code):
        self.name = string(name)
        # Name; e.g.: Boeing 757

        self.f_code = string(f_code)
        ###
        # Flight code; e.g: VN457
        # To be sychronised with Passenger through Flight class
        ###

    ###
    # Setter and getters
    ###
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setCode(self, code):
        self.f_code = code
    def getCode(self):
        return self.f_code



class Flight:
    def __init__(self, f_code, 
    n_passenger, list_passenger, 
    plane,
    t_depart, t_arrive, 
    p_depart, p_arrive,
    ):
        
        self.f_code = string(f_code)
        ###
        # Flight code; e.g: VN457
        # To be sychronised with Passenger and Plane
        ###

        self.plane = plane
        ###
        # Import plane name from f_code
        # Used for printing out information about flight
        ###

        self.n_passenger = int(n_passenger)
        self.list_passenger = list_passenger
        ###
        # Variables to manage passenger
        # n_passenger for number of passenger
        # list_passenger is Dict/List/Array type for seats and passengers
        ###

        self.t_depart = int(t_depart)
        self.t_arrive = int(t_arrive)
        ###
        # Variables for depart and arrive time
        # Use 24hr format
        ###

        self.p_depart = string(p_depart)
        self.p_arrive = string(p_arrive)
        ###
        # Variables for depart and arrive location
        # Use format: City, Country
        ###

        self.flights = []
        # Flight list

    def validateTime(self, t):
        if t in range(0, 24):
            return True
        else:
            return False
    # Validate function for time, used for both depart and arrive
    
    def seatlimit(self, n_passenger):
        if n_passenger in range(0, 120):
            return True
        else:
            return False
    # Used to check to avoid overbooking
    
    def seats_to_pickle(self):
    #load seat into pickle file
        seats = {
            'business': {'1A', '1B', '1C', '1D', '1E', '1F', '2A', '2B', '2C', '2D', '2E', '2F', '3A', '3B', '3C', '3D', '3E', '3F', '4A', '4B', '4C', '4D', '4E', '4F'},
            'eco': {'5A', '5B', '5C', '5D', '5E', '5F', '6A', '6B', '6C', '6D', '6E', '6F', '7A', '7B', '7C', '7D', '7E', '7F', '8A', '8B', '8C', '8D', '8E', '8F', '9A', '9B', '9C', '9D', '9E', '9F', '10A', '10B', '10C', '10D', '10E', '10F', '11A', '11B', '11C', '11D', '11E', '11F', '12A', '12B', '12C', '12D', '12E', '12F', '13A', '13B', '13C', '13D', '13E', '13F', '14A', '14B', '14C', '14D', '14E', '14F', '15A', '15B', '15C', '15D', '15E', '15F', '16A', '16B', '16C', '16D', '16E', '16F', '17A', '17B', '17C', '17D', '17E', '17F', '18A', '18B', '18C', '18D', '18E', '18F', '19A', '19B', '19C', '19D', '19E', '19F', '20A', '20B', '20C', '20D', '20E', '20F'}
                }
        if not path.exists('flight_data'):
            self.load_data('flight_data', seats)
            
    def load_data(self, file_name, objects):
    # Func to load pickle data
        with open(file_name, 'wb') as open_file:
            pickle.dump(objects, open_file)
            
    def open_pickle(self):
    # Func to open and return pickle data
        if path.exists('flight_data'):
            with open('flight_data', 'rb') as seats:
                return pickle.load(seats)
        else:
            return {}
    
    def check_class(self, checkclass):
    # Func to check class (1 for Business and 2 for Economy)
    # Return 1 if class is available, 0 if n/a and 2 if all seats are booked
        seats_all = self.open_pickle()
        if len(seats_all) > 0:
            if checkclass == 1 and len(seats_all['business']) == 0:
                return 0
            elif checkclass == 2 and len(seats_all['eco']) == 0:
                return 0
            else:
                return 1
        else:
            return 2

    def check_seat(self, seat_class):
    # Check seat available or not (0 is n/a, 1 is available, 2 is all are n/a)
        seats_all = self.open_pickle()
        seat_list = list()
        seat_dict = dict()
        if len(seats_all) > 0:
            if seat_class == 1 and len(seats_all['business']) > 0:
                for i in seats_all['business']:
                    seat_list.append(sorted(seats_all['business'][i]))
                if seat_class not in seat_dict:
                    seat_dict[seat_class] = seat_list
                for i in seat_dict[seat_class]:
                    if len([j for j in i if j.endswith('A') or j.endswith('B') or j.endswith('C') or j.endswith('D') or j.endswith('E') or j.endswith('F')]) > 0:
                        return 1
                    else:
                        return 0

            if seat_class == 2 and len(seats_all['eco']) > 0:
                for i in seats_all['eco']:
                    seat_list.append(sorted(seats_all['eco'][i]))
                if seat_class not in seat_dict:
                    seat_dict[seat_class] = seat_list
                for i in seat_dict[seat_class]:
                    if len([j for j in i if j.endswith('A') or j.endswith('B') or j.endswith('C') or j.endswith('D') or j.endswith('E') or j.endswith('F')]) > 0:
                        return 1
                    else:
                        return 0
        else:
            return 2
            

    def auto_booking(self, seat_class):
    # func to auto booking seat for each class
        with open('flight_data', 'rb') as seats:
            alls = pickle.load(seats)
        if seat_class == 1:
            n = random. randint(1, 4)
            return "".join([j for j in alls['business'][n] if j.endswith('A') or j.endswith('B') or j.endswith('C') or j.endswith('D') or j.endswith('E') or j.endswith('F')][0])
        
        if seat_class == 2:
            n = random. randint(5, 20)
            return "".join([j for j in alls['eco'][n] if j.endswith('A') or j.endswith('B') or j.endswith('C') or j.endswith('D') or j.endswith('E') or j.endswith('F')][0])


    def take_seat(self, seat_class, seat):
    # Take seat and load booked ones in pickle file
        booked = dict()
        if path.exists('booked_seats'):
            with open('booked_seats', 'rb') as reseats:
                booked = pickle.load(reseats)
        
        with open('flight_data', 'rb') as seats:
            alls = pickle.load(seats)

            if seat_class ==1:
                if seat not in alls.values() and seat_class not in alls.keys():
                    alls['business'][seat_class] = [seat]
                else:
                    alls['business'][seat_class].append(seat)
                if seat in alls['business'][int(seat[0])]:
                            alls['business'][int(seat[0])].discard(seat)
            
            if seat_class == 2:
                if seat not in alls.values() and seat_class not in alls.keys():
                    alls['eco'][seat_class] = [seat]
                else:
                    alls['eco'][seat_class].append(seat)
                if seat in alls['eco'][int(seat[0])]:
                            alls['eco'][int(seat[0])].discard(seat)
        
        with open('flight_data', 'wb') as seats:
            pickle.dump(alls, seats)    
            
        if not path.exists('booked_seats'):
            self.load_pickle('booked_seats', booked)
        elif path.exists('booked_seats'):
            self.load_pickle('booked_seats', booked)

    def initArray():
        SeatArray = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],]
        return SeatArray
    # Return an 2D array of completely empty seats, set the 

    def SeatAutofill(self, array, lpassenger):
        temparr = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],]
        for x in range(0, len(lpassenger)):
            tempnum = lpassenger[x].getSeat()
            temp = ''
            tempchar = ''
            intchar = -1
            for y in range(0, len(string.ascii_uppercase)):
                tempchar = string.ascii_uppercase[y]
                if (tempnum[1] == tempchar) or (tempnum[2] == tempchar):
                    temp = tempnum.replace(tempchar, '')
                    intchar = y
            temp = int(temp)
            array[temp][intchar] = 1
            temparr[temp][intchar] = lpassenger[x].getName()
        self.list_passenger = temparr
    ###
    # Function to fill the list of passenger of flight according to an external list of passenger
    ###
    
    def input(self):
    # Input flight info
        f_code = str(input())
        plane = str(input())
        t_depart = int(input())
        t_arrive = int(input())
        p_depart = str(input())
        p_arrive = str(input())
        flight = {
            "f_code" : f_code,
            "plane" : plane,
            "t_depart" : t_depart,
            "t_arrive" : t_arrive,
            "p_depart" : p_depart,
            "p_arrive" : p_arrive
        }
        return flight

    def changeTime(self, flights):
    # change depart and arrive time of selected flight
        selected_flight = str(input())
        for i in range(len(flights)):
            if selected_flight == flights[i]['f_code']:
                flights[i]['t_depart'] = int(input)
                flights[i]['t_arrive'] = int(input)
        return flights
    
    ###
    # Setter and getters
    ###
    def setCode(self, code):
        self.f_code = code
    def getCode(self):
        return self.f_code

    def set_npass(self, n):
        self.n_passenger = n
    def get_npass(self):
        return self.n_passenger
    def set_lpass(self, l):
        self.list_passenger = l
    def get_lpass(self):
        return self.list_passenger

    def setPlane(self, plane):
        self.plane = plane
    def getPlane(self):
        return self.plane

    def setTD(self, td):
        self.t_depart = td
    def getTD(self):
        return self.t_depart 
    def setTA(self, ta):
        self.t_arrive = ta
    def getTA(self):
        return self.t_arrive

    def setPD(self, pd):
        self.p_depart = pd
    def getPD(self):
        return self.p_depart
    def setPA(self, pa):
        self.p_arrive = pa
    def getPA(self):
        return self.p_arrive 

    def setFlights(self, f):
        self.flights = f
    def getFlights(self):
        return self.flights  

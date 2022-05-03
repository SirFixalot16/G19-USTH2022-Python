import string
import pickle
from os import path

class Passenger:
    def __init__(self, name, pid, f_code, seat):
        self.name = (name) 
        # Name; e.g.: Vu Quoc Thai
        self.pid = (pid) 
        # Personal ID; e.g.: 001202001264

        self.f_code = (f_code)
        # Flight code; e.g: VN457
        self.seat = (seat)
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
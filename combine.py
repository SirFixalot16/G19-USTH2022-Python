import domains
import string

###
# This class exists only to export a location String for p_depart and p_arrive variables
###
class Location:
    def __init__(self, ct, pays):
        self.ct = string(ct)
        # City
        self.pays = string(pays)
        # French for country


    def validateCT(self, ct_list, ct):
        for x in range(0, len(ct_list)):
            tempct = ct_list[x]
            if ct == tempct:
                return True

    def validatePays(self, pays_list, pays):
        for x in range(0, len(pays_list)):
            tempp = pays_list[x]
            if pays == tempp:
                return True

    ###
    # Setter and getters
    ###    
    def setCT(self, ct):
        self.ct = ct
    def getCT(self):
        return self.ct
    def setPays(self, pays):
        self.pays = pays
    def getPays(self):
        return self.pays

    def export(self):
        return (self.ct +', ' + self.pays)
    # Somehow the most important function



###
# This class exists only to export a seat code, i.e.: 9F, 20A
###
class Seats:
    def __init__(self, letter, num):
        self.letter = string(letter)
        self.num = int(num)

    ###
    # Setter and getters
    ###    
    def setLetter(self, l):
        self.letter = l
    def getLetter(self):
        return self.letter
    def setNum(self, n):
        self.num = n
    def getNum(self):
        return self.num

    def validateSeats(self, l, n):
        if n in range(1, 20):
            for x in range(0, 5):
                tempstr = string.ascii_uppercase[x]
                if l == tempstr:
                    return True

    def export(self):
        return (str(self.num) + self.letter)
    # Somehow the most important function, again

    
    

def main():
    EligibleCT = ("Hanoi", "Saigon")
    # City tuple
    EligiblePays = ("Vietnam")
    # Country tuple

    SeatArray = [[0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]]
    # Seat 2D array



if __name__ == "__main__":
    main()
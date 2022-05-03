import string

###
# This class exists only to export a seat code, i.e.: 9F, 20A
###
class Seats:
    def __init__(self, letter, num):
        self.letter = (letter)
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
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


    def returnCT(self, pays):
        ct_list = []
        match pays:
            case 'Vietnam':
                ct_list = ['Hanoi', 'Saigon', 'Da Nang', 'Phu Quoc', 'Hue', 'Da Lat', 'Nha Trang', 'Ca Mau', 'Con Dao']
            case 'Japan':
                ct_list = ['Tokyo', 'Nagoya', 'Osaka', 'Fukuoka']
            case 'Korea':
                ct_list = ['Seoul', 'Busan']
            case 'China':
                ct_list = ['Guangzhou', 'Shanghai', 'Chengdu', 'Beijing', 'Hong Kong', 'Taipei', 'Macau']
            case 'Thailand':
                ct_list = ['Bangkok', 'Phuket']
            case 'Singapore':
                ct_list = ['Singapore']
            case 'Indonesia':
                ct_list = ['Jakarta', 'Bali']
            case 'Phillipines':
                ct_list = ['Manila']
            case 'Myanmar':
                ct_list = ['Yargon']
            case 'Malaysia':
                ct_list = ['Kuala Lumpur']
            case 'Laos':
                ct_list = ['Luang Prabang']
            case 'Campuchia':
                ct_list = ['Siem Reap', 'Phnom Phenh']
            case _:        
                ct_list = ['Error']
        return ct_list

    def validatePays(self, pays):
        pays_list = ("Vietnam", "Japan", "Korea", "China", "Thailand", "Singapore", "Indonesia", "Phillipines", "Myanmar", "Malaysia", "Laos", "Campuchia")
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
    l = []

if __name__ == "__main__":
    main()
import string

###
# This class exists only to export a location String for p_depart and p_arrive variables
###
class Location:
    def __init__(self, ct, pays):
        self.ct = (ct)
        # City
        self.pays = (pays)
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
            case 'Cambodia':
                ct_list = ['Siem Reap', 'Phnom Penh']
            case _:        
                ct_list = ['Error']
        return ct_list

    def validatePays(self, pays):
        pays_list = ("Vietnam", "Japan", "Korea", "China", "Thailand", "Singapore", "Indonesia", "Phillipines", "Myanmar", "Malaysia", "Laos", "Cambodia")
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
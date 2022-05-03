import string

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
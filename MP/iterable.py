class Building(object):
    def __init__(self, floors):
        self.__floors = [None] * floors

    def __setitem__(self, floor_num, data):
        self.__floors[floor_num] = data

    def __getitem__(self, floor_num):
        return self.__floors[floor_num]


building_1 = Building(4)
building_1[0] = "Room One"
building_1[1] = "Room Two"
building_1[2] = "Room Three"
building_1[2] = "Room Top"

for thing in building_1:
    print(thing)

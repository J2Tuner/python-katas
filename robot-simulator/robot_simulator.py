class Robot(object):
    bearing = None
    bearings = {"NORTH":0, "EAST":1, "SOUTH":2, "WEST":3}
    coordinates = None
    
    def __init__(self, bearing = "NORTH", xCoord = 0, yCoord = 0):
        self.bearing = bearing
        self.coordinates = (xCoord, yCoord)

    def advance(self, steps = 1):
        xCoord = self.coordinates[0]
        yCoord = self.coordinates[1]
        if self.bearing == "NORTH":
            yCoord += steps
        elif self.bearing == "EAST":
            xCoord += steps
        elif self.bearing == "SOUTH":
            yCoord -= steps
        else: #WEST
            xCoord -= steps
        self.coordinates = (xCoord, yCoord)

    def turn_left(self, turns = 1):
        self._turn(turns, -1)        

    def turn_right(self, turns = 1):
        self._turn(turns, 1)            

    def _turn(self, turns, direction):
        # Turn and set new bearing
        bearingValue = self.bearings[self.bearing]
        bearingValue = (bearingValue + (turns * direction)) % 4
        for cardinal, value in self.bearings.items():
            if value == bearingValue:
                self.bearing = cardinal

    def simulate(self, instructions):
        for i in instructions:
            if i == 'L':
                self.turn_left()
            elif i == 'R':
                self.turn_right()
            elif i == 'A':
                self.advance()


NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"

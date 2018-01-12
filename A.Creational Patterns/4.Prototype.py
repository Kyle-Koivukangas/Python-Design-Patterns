# A prototype pattern is meant to specify the kinds of objects to use a prototypical instance, 
# and create new objects by copying this prototype.

# A prototype pattern is useful when the creation of an object is costly 
# EG:   when it requires data or processes that is from a network and you don't want to 
#       pay the cost of the setup each time, especially when you know the data won't change.

from copy import deepcopy

class Car: 
    def __init__(self):
        self.__wheels   = []
        self.__engine   = None
        self.__body     = None
    
    def setBody(self, body):
        self.___body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print(f"body: {self.__body.shape}")
        print(f"engine horsepower: {self.__engine.horsepower}")
        print(f"tire size: {self.__wheels[0].size}")

    #it's pretty similar to the builder pattern, except you have a method that will easily allow you to copy the instance
    # this stops you from having to 
    def clone(self):
        return deepcopy(self)

# Here is another separate example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f"({self.x}, {self.y})")

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        """ This clone method allows you to clone the object but it also allows you to clone it at a different point on the plane """
        obj = deepcopy(self)
        obj.move(move_x, move_y)

        return obj

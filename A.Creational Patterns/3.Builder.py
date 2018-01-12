# A builder is meant to separate the constructions of a complex object from its representation 
# so that the same construction process can create different representations.

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


# === Car parts ===
class Wheel:
    size = None

class Engine:
    horsepower = None
    
class Body:
    shape = None


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    
    # The algorithm for assembling a car
    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)


        # Then the engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)


        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)

        return car


class BuilderInterface:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass

# This is a set of build instructions for a specific kind of car using all the builder components above to actually make it.
class jeepBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

#build instructions for another type of car
class NissanBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 17
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 300
        return engine

    def getBody(self):
        body = Body()
        body.shape = "Sedan"
        return body


# TO use the Builder:

# Instantiate the director class
d = Director()

# Set the build profile you want to use
d.setBuilder(jeepBuilder())

# Build car, save car instance
d.getCar()
# jeep = d.getCar()

# List car specs
d.getCar().specification()

#try with another car
d2 = Director()
d2.setBuilder(NissanBuilder())
d.getCar().specification()

# The adapterpattern converts the interface of a class into another interface clients expect.
# Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

# adaptee (source) interface
class EuropeanSocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass
    def earth(self): pass

# Target interface
class USASocketInterface:
    def voltage(self): pass
    def live(self): pass
    def neutral(self): pass

# Adaptee
class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0

# Client
class AmericanKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 100:
            print("Kettle on fire!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Coffee time!")
            else:
                print("No power.")

# How to make the European socket useable for the american kettle?
# we will use an adapter pattern:

class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        # adapter will override the voltage to 100V
        return 110

    def live(self):
        # live value doesn't need to be adjusted, returns original value
        return self.__socket.live()

    def neutral(self):
        # neutral value doesn't need to be adjusted, return original value
        return self.__socket.neutral()



# Example of adapter in use:

# Try running boil() just using european socket:
socket = EuropeanSocket()
kettle = AmericanKettle()

kettle.boil() # "Kettle on fire!"

#try running boil() using the american socket adapter:
adapter = Adapter(socket)
kettle = AmericanKettle(Adapter)

kettle.boil() # "Coffee Time!"



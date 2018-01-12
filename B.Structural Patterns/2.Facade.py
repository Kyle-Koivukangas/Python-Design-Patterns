# A facade pattern provides a unified interface to a set of interfaces in a subsystem.
# A facade defines a higher-level interface that makes the subsystem easier to use.

# An API is essentially a facade pattern, it allows you to make calls to the facade(API) without
# actually neeeding to know how the commands are carried out, it is a level of abstraction
# that makes working with a libaray or tool much easier.

# A Facade pattern can:
#       - Make a library easier to use, understand and test, since the facade has convenient methods for common tasks
#       - Reduce dependencies of outside code on the inner workings of a library, allowing more flexibility in developing the system
#       - Wrap a poorly designed collection of APIs with a single well-designed API

#Example:

class Engine:
    def __init__(self):
        #how much the motor is spinning in RPM
        self.spin = 0

    def start(self, spin):
        self.spin = min(spin, 3000)

class StarterMotor:
    def __init__(self):
        #How much the starter motor is spinning in RPM
        self.spin = 0
    
    def start(self, charge):
        #if there is enough power then spin fast
        if charge > 50:
            self.spin = 2500

class Battery:
    def __init__(self):
        # % charged, starts flat
        self.charge = 0

class Car:
    # The facade object tyhat deals with the battery, engine and starter motor
    def __init__(self):
        self.battery = Battery()
        self.starter = StarterMotor()
        self.engine = Engine()

    def turn_key(self):
        #   This is a command for the facade that will enact the turn_key() process which will start the car.
        #   In this example, the car won't start unless the battery has a charge first, so you will need to
        # call the method jump() first
        self.starter.start(self.battery.charge)
        self.engine.start(self.starter.spin)
        if (self.engine.spin > 0):
            print("Engine starter")
        else:
            print("Engine NOT starred")
        
    def jump(self):
        # jump the car to add charge to the battery
        self.battery.charge = 100
        print("jumped")

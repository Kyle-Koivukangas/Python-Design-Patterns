# The singleton pattern ensures that a class has only one instance, and provides a global point of access to it, for example, a logging class
# The borg idiom (A.K.A. monostate pattern) lets a class have as many instances as one likes, but ensures that they all share the same state

# __new__ is the first step of instance creation; it's calle before __init__ and is responsible for returning a new instance of your class
# __init__ doesnt return anything; it's only responsible for initializing the instance after it's been created

class Singleton:
    __instance = None
    def __new__(cls, val=None):
        """ check to see if __new__ is none (if there is already an instance of the singleton class); if so, then it will set it to a new object of the singleton class
            Once the class has been instantiated once, every try to instantiate it again will always return the same original object and it won't allow you to make duplicate instances.
        """
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


class Borg:
    __shared_state = {}
    def __init__(self):
        """ Borg is different from Singleton in that you can set multiple instances of the same class, they will be truly separate objects, 
            but they will share their state as if they were the same object .
        """
        self.__dict___ = self.__shared_state


# PROS and CONS:
# Singleton:  PROS    - Singletons are allocated once and only once.
#                     - Policies can be added to the method that provides access to the singleton pointer.

#             CONS    - Derivatives of Singletons are not automatically Singletons.
#                     - Singletons must always be accessed through a pointer or reference (obtaining this has overhead)


# Borg:       PROS    - Derivatives of Monostate/Borg classes can also be monostate.
#                     - Access to monostate objects does not have to be through pointers or references.
            
#             CONS    - No instantiation policy can exist for Monostate classes.
#                     - Monostate instances may be allocated and deallocated many times. (bad for memory heavyyy instances)

# NOTE: Python modules are singletons but it is not recommended to use them as a way of making a class a singleton.




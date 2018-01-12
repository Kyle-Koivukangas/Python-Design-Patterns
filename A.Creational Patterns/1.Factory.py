# A factory is meant to define an interface for creating an object, but defer the object instantiation to run time.

# NOTE: An interface just defines the methods where as an abstract base class will also define the attributes that the subclasses will use
class ShapeInterface:
    def draw(self): pass


# Below are two concrete subclasses of the shape interface
class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")

class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")


class ShapeFactory:
    @staticmethod
    def getShape(type):
        if type == "circle":
            return Circle()
        if type == "square":
            return Square()
        
        assert 0, f"Could not find {type}"


#   ABSTRACT FACTORY:               ------------------------------------------------------------------------------

# An abstract factory provides an interface for creating families of related objects without specifying their concrete classes.

# === abstract shape classes ===
class Shape2DInterface:
    def draw(self): pass

class Shape2DInterface:
    def draw(self): pass


# === concrete shape classes ===
class Circle(Shape2DInterface):
    def draw(self): 
        print("Circle.draw")

class Square(Shape2DInterface):
    def draw(self): 
        print("Square.draw")

class Sphere(Shape3DInterface):
    def draw(self): 
        print("Sphere.draw")

class Cube(Shape3DInterface):
    def draw(self): 
        print("Cube.draw")
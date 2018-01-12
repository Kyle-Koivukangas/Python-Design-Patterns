# An abstract factory provides an interface for creating families of related objects without specifying their concrete classes.
# it's basically just another level of abstraction on top of a normal factory

# === abstract shape classes ===
class Shape2DInterface:
    def draw(self): pass

class Shape3DInterface:
    def build(self): pass


# === concrete shape classes ===
class Circle(Shape2DInterface):
    def draw(self): 
        print("Circle.draw")

class Square(Shape2DInterface):
    def draw(self): 
        print("Square.draw")

class Sphere(Shape3DInterface):
    def draw(self): 
        print("Sphere.build")

class Cube(Shape3DInterface):
    def draw(self): 
        print("Cube.build")


# === Abstract shape factory ===
class ShapeFactoryInterface:
    def getShape(self, sides): pass


# === Concrete shape factories ===
class Shape2DFactory(Shape2DInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, f"Bad 2D shape creation: shape not defined for {sides} sides"

class Shape3DFactory(Shape3DInterface):
    @staticmethod
    def getShape(sides):
        """technically, sides refers to faces"""
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, f"Bad 3D shape creation: shape not defined for {sides} sides"


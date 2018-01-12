# A decorator pattern is meant to be able to attach additional responsibilities to an 
# object dynamically. 
# Decorators provide a flexible alternative to subclassing for extending functionality.

# Rather than using subclasses to alter how a class/object behaves, a decorator pattern 
# allows you to make changes much more simply with greater flexibility, you can simply attach any 
# combination of decorators to an object rather than having a complicated tree of subclasses.


class WindowInterface:
    def build(self): pass

class AbstractWindowDecorator(WindowInterface):
    """
    Maintain a reference to a window object and define an interface
    that conforms to Window's interface.
    """

    def __init__(self, window):
        self._window = window
    
    def build(self): pass


class Window(WindowInterface):
    def build(self):
        print("Building window")
    
class BorderDecorator(AbstractWindowDecorator):
    def add_border(self):
        print("adding border")
    
class VerticalSBDecorator(AbstractWindowDecorator):
    def add_vertical_scroll_bar(self):
        print("Adding vertical scroll bar")
    
    def build(self):
        self.add_vertical_scroll_bar()
        self._window.build()
    
class HorizontalSBDecorator(AbstractWindowDecorator):
    def add_horizontal_scroll_bar(self):
        print("Adding Horizontal scroll bar")

    def build(self):
        self.add_horizontal_scroll_bar()
        self._window.build()

# Examples of the decorator patterns in use:

#instantiate the window object:
w = Window()
w.build() # "Buiding window"

# Instantiate a window object with border:
# We instantiate a border decorator and pass it a window to apply it to.
wb = BorderDecorator(w)
wb.build() # "Adding border" \n "Building window"

#add a vertical scroll bar to this:
# We instantiate a verticalSBDecorator and pass is the window we want to add it to.
wbv = VerticalSBDecorator(wb)
wbv.build() # "adding vertical scrollbar" \n "Adding border" \n "Building window" 

# You can add as many decorators as you want to the object this way.
# window with all the decorators applied

everything_window = HorizontalSBDecorator(wbv)
everything_window.build() #  "adding horizontal scrollbar" \n "adding vertical scrollbar" \n "Adding border" \n "Building window" 

#NOTE: Decorator design pattern != python decorator/function wrapper. The two are not the same.
#       They are similar but Python decorators/function wrappers only apply to functions/methods 
#       Whereas the decorator design pattern applies specifically to classes. 

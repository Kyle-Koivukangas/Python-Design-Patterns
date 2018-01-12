# A proxy provides a surrogate of place holder to provide access to an object.

# Why use a proxy?
#   - It allows you to use an extra level of indirection to support distributed, 
#       controlled or conditional access. (Like if the object needs authorization to be accessed)
#   - It also allows you to add a wrapper and delegation to protect the real component 
#       from undue complexity. EG: say your authorization object is fairly complex, it would 
#       not be a good idea to add it to the actual component because it already has it's own responsiblity
#       So encapsulating the object in a proxy would be a better idea than mixing it all in to one object
#       and causing needless complexity.

#Example:

class SubjectInterface:
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """

    def request(self): pass


class Proxy(SubjectInterface):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """
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

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy mayy be doing something, like controlling request access here.")
        self._real_subject.request()


class RealSubject(SubjectInterface):
    """
    Define the real object that the proxy represents.
    """

    def request(self):
        print("The real thing is dealing with the request.")

#How to use:

#instantiate the RealSubject object
rs = RealSubject()

# rs.request() prints "The real thing is dealing with the request"

#then, instantiate the proxy, through which we will access the real object
proxy = Proxy(rs)

#proxy.request() prints "Proxy mayy be doing something, like controlling request access here."
#                       "The real thing is dealing with the request."

# The proxy will execute its authorization or peermissions code before calling the actual object.
# This example of how to implement a proxy pattern using a common interface (SubjectInterface)


# The next example will use a common proxy class and we will subclass it
#Example 2:

class Blog:
    def read(self):
        print('read the blog')

    def write(self):
        print('Write the blog')

class Proxy:
    def __init__(self, target):
        self.target = target
    
    def __getattr__(self, attr):
        return getattr(self.target, attr)

class AnonUserBlogProxy(Proxy):
    def __init__(self, blog):
        super().__init__(blog)
    def write(self):
        print("Onlyy authorized userss can write blog posts")

# The proxy and the blog classes do not chare an interfaace, 
# the proxy is generic and could be a proxy for any object

# The sublass of Proxy (AnonUserBlogProxy) sets the target to be the blog object and
# the write method is overwritten to print that only authorized users can write a post.

# How it's used:

#instantiate the blog object
blog = Blog()

blog.write() #prints "Write the blog"

#instantiate the proxy with the blog object as it's target
proxy = AnonUserBlogProxy(blog)

proxy.write() #prints  "Only authorized users can write blog posts"

#The advantage of using this second method is that the proxy is a generic class that can be used
# for multiple objects, whereas in the first example the proxy is only able to be used for the
# particular object that it was created for and depends on the common interface that they share.

#The first method is much more explicit, but the second method gives you a lot more felxibility
# in how the proxy will be used.

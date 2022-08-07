'''Multiple inheritance and "MRO" example. 
   More information about "MRO" -> https://tirinox.ru/mro-python/ '''

class A(object):
    def name(self):
        print("I'm A")


class B(A):
    def name(self):
        print("I'm B")


class C(A):
    def name(self):
        print("I'm C")


'''You can inherit from class b and c but you can't inherit from class a'''
class D(B, C):
    def name(self):
        print("I'm D")
        
        
# This is a mistake

'''
class D(A, B):
    def name(self):
        print("I'm D")
'''

'''
class D(A, C):
    def name(self):
        print("I'm D")
'''


def print_mro(T):
    '''It's function "print_mro" for to write only class names'''
    print(*[c.__name__ for c in T.mro()], sep=' -> ')


print_mro(D)
#print(D.__mro__)
# d = D()
# d.name()
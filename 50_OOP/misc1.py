# Script con algunas magic functions
# pruebalo en el python interpreter CLI
class Numero():
    def __init__(self,num_x):
        self.num_x = num_x
    def __int__(self):
        return (int(self.num_x))
    def __str__(self):
        return (str(self.num_x))
    def __repr__(self):
        return (repr(self.num_x))
    def __add__(self,other):
        return (self.num_x + other)

n = Numero(10)
print (n)
n
repr(n)
n+10


from math import pi
def add (n1,n2):
    return n1+n2
def area_of_circle(r):
    if r < 0:
        raise ValueError("Negative radius value error")
    else:
        return (pi*(r**2))

#print (area_of_circle(1))
#print (area_of_circle(-1))

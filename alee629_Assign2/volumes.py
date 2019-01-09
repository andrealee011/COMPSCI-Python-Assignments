#Assignment 2: Volume Calculator
#Andrea Lee 250836721

#import math to get pi for ellipsoid volume
import math


#define volume function for each shape
def cube_volume(a):
    #prompt user for dimensions
    a = int(input('Enter side:\n'))
    #calculate volume
    volume = a*a*a
    #print message
    print('The volume of a cube with side %.2f is: %.2f' % (a, volume))
    #return volume to be later stored in a list
    return volume


def pyramid_volume(b, h):
    b = int(input('Enter base:\n'))
    h = int(input('Enter height:\n'))
    volume = ((1/3)*b*b*h)
    print('The volume of a pyramid with base %.2f and height %.2f is: %.2f' % (b, h, volume))
    return volume


def ellipsoid_volume(r):
    r = int(input('Enter radius:\n'))
    volume = ((4/3)*math.pi*r*r*r)
    print('The volume of an ellipsoid with radius %.2f is: %.2f' % (r, volume))
    return volume

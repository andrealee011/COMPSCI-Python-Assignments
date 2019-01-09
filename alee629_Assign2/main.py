#Assignment 2: Volume Calculator
#Andrea Lee 250836721

#import volumes to get volume function for each shape
import volumes

#create list for each shape that volumes will be added to
cube_list = []
pyramid_list = []
ellipsoid_list = []

#define variables
a = 0
r = 0
b = 0
h = 0

#prompt user for shape
shape_input = input('Enter shape:\n')

#loop until user inputs quit
while shape_input.lower() not in ['q', 'quit']:

    #calculate volume for shape, print message and add volume to list for shape
    if shape_input.lower() in ['c', 'cube']:
        cube_list.append(float(volumes.cube_volume(a)))
        shape_input = input('\nEnter shape:\n')

    elif shape_input.lower() in ['p', 'pyramid']:
        pyramid_list.append(float(volumes.pyramid_volume(b, h)))
        shape_input = input('\nEnter shape:\n')

    elif shape_input.lower() in ['e', 'ellipsoid']:
        ellipsoid_list.append(float(volumes.ellipsoid_volume(r)))
        shape_input = input('\nEnter shape:\n')

    #continue prompting user for shape if user input is invalid
    else:
        shape_input = input('\nEnter shape:\n')

#sort list of volumes for each shape
cube_list.sort()
pyramid_list.sort()
ellipsoid_list.sort()

#print output
print('\nYou have reached the end of your session.')

#if all lists are empty print message
if len(cube_list) == 0 and len(pyramid_list) == 0 and len(ellipsoid_list) == 0:
    print('You did not perform any volume calculations.')

#print sorted list of volumes for each shape or print message if list is empty
else:
    print('The volumes calculated for each shape are:')
    print('Cube:', end=' ')
    if len(cube_list) == 0:
        print('No shapes entered')
    else:
        for i in cube_list [:-1]:
            print('%.2f,' % i, end=' ')
        print('%.2f' % cube_list[-1])

    print('Pyramid:', end=' ')
    if len(pyramid_list) == 0:
        print('No shapes entered')
    else:
        for i in pyramid_list [:-1]:
            print('%.2f,' % i, end=' ')
        print('%.2f' % pyramid_list[-1])

    print('Ellipsoid:', end=' ')
    if len(ellipsoid_list) == 0:
        print('No shapes entered')
    else:
        for i in ellipsoid_list [:-1]:
            print('%.2f,' % i, end=' ')
        print('%.2f' % ellipsoid_list[-1])


#Program 7                            #ALIZAR

a=int(input('Enter The First Angle : '))
b=int(input('Enter The Second Angle : '))
def thirdangle(angle1,angle2):
    angle3=180-angle1-angle2
    return angle3
print('Third Angle Of Triangle Is : ',thirdangle(a,b))

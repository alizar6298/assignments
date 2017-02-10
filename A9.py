#Program 9                                    #ALIZAR

print("Enter The Marks Obtained From 100 :")
s1=int(input('Enter The Marks Of OOAD : '))
s2=int(input('Enter The Marks Of DMBS : '))
s3=int(input('Enter The Marks Of Python : '))
s4=int(input('Enter The Marks Of NAMS : '))
s5=int(input('Enter The Marks Of Microprocesser : '))
mean=(s1+s2+s3+s4+s5)/5
print('Mean Of Marks Is : ',mean)
perc=mean
if perc<35:
    print('You Are Fail(Hayla Rakhe Bhura)')
    print('Your Percetage Are : ',perc)
else:
    print('You Are Pass(Party Aap Hal)')
    print('Your Percentage Are : ',perc )

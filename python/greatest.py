'''a=int(input('enter the number a:'))
b=int(input('enter the number b:'))
c=int(input('enter the number c:'))
if a>b and a>c:
    print('a is the greatest number')
elif b>c:
    print('b is greatest number')
else:
    print('c is greatest number')'''

marks=int(input('enter the marks:'))
if marks>= 91 and marks<=100:
    print('grade A')
elif marks>=71 and marks<=89:
    print('grade B')
elif marks>=51 and marks<=69:
    print('grade c')
else:
    print('Fail')
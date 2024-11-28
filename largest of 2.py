print('Enter three numbers')
a=int(input())
b=int(input())
c=int(input())

if a>b:
    if a>c:
        print(f'{a} is the largest')
    else:
        print(f'{c} is the largest')

else:
    if b>c:
        print(f'{b} is the largest')
    else:
        print(f'{c} is the largest')

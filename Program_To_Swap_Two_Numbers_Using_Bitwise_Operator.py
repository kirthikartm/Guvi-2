''' PROGRAM TO SWAP TWO NUMBERS USING BITWISE OPERATOR '''
a,b=input().split()
a=int(a)
b=int(b)
a=a^b
b=a^b
a=a^b
print(a,b)

''' проверка на полиндром строку
полиндром - это строка атататата она читается
одинаково и с начала и с конца'''
s=input()
i=0
j=len(s)-1
is_palindrom=True
while i<j :
    if s[i]!=s[j]:
        is_palindrom=False
        break
    i+=1
    j-=1
print(is_palindrom)

'''минус 2 способа в создании новой строки и экономии памяти '''
s=input()
r=s[::-1]
if s==r:
    print('равны')
else :
    print('не равны ')
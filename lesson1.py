a,b=int(input()),int(input())
i=0
if a==b :
    s=a
elif a<b :
    i=a
else :
    i=b

if a!=b :
    while i<a*b :
        if i%a==0 and i%b==0 :
            s=i
            break
        else    :
            i+=1
            s=a*b
print(s)

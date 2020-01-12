'''
Узнав, что ДНК не является случайной строкой,
только что поступившие в Институт биоинформатики студенты
группы информатиков предложили использовать алгоритм сжатия,
который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной строки
заменяются на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом
и выводит закодированную последовательность на стандартный вывод.
Кодирование должно учитывать регистр символов.
'''
s=input()
dnk=''
i=0
while i<len(s) :
    j=i
    n=1
    while j<len(s)-1 :
        if s[j]==s[j+1] :
            n+=1
            j+=1
            i=j
        else :
            i=j
            break
    dnk=dnk+s[i]+str(n)
    i+=1
print(dnk)

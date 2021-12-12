# # найти делитель для числа 64
from math import sqrt
n = 64
пустой список делителей
de = []
# до какого значения будем перебирать
q = round(sqrt(n)) # окруляем к ближающему целому значению
# проверим, является ли число квадратом
# возводим окрукленное значение корня квадрат и если оно даст мне исходное число, значит наше окруление на наш корень не повлияло
if q * q == n:
    de.append(q)
for i in range(1, q):
    if n % i == 0:
        de.append(i)
        #парные число
        de.append(n // i)
print(*sorted(de))

# 2
from math import sqrt
chet = 0
for i in range(3532000, 3532160+1):
#     создадим счетчик делителей
    cnt = 0
    q = round(sqrt(i))
    for d in range(2, q + 1):
        if i % d == 0:
            cnt += 1
            if cnt > 0:
                break
    if cnt == 0:
        chet += 1
        print(chet, i)

# 3
нужно найти кол-во делителей
from math import sqrt
for i in range(174457, 174505+1):
    # пустой список делителей
    divs = []
    q = round(sqrt(i))
    for d in range(2, q + 1):
        # если нашли делитель
        if i % d == 0:
            # то добавляем сам делитель и пару для него
            divs += [d , i // d] # по аналогии divs.append(numbers)
    # нашли ровно два различных делителя
    if len(set(divs)) == 2:
        print(*set(sorted(divs)))

# 4
for i in range(2031, 14312 + 1):
    x = i
    ok = True
    while x > 0:
        if x % 11 == 2:
            ok = False
            break
        else:
            x //= 11
    if ok:
        maxch = max(maxch, i)
print(maxch)

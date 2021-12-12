# x = 64 ** 10 + 2 ** 90 - 16
# print(oct(x)[2::].count('7'))

s = 4**2016 + 2**2016 - 15
count = 0

while s > 0:
    if s % 2 == 1:
        count += 1
    s = s // 2

print(count)
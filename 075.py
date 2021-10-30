numbers = [111, 222, 333, 444]
for a in numbers:
    print(a)
num = int(input('chislo: '))
if num in numbers:
    print(numbers.index(num))
else:
    print('error:')
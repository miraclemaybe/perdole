party = []
for i in range(3):
    n = input('imya: ').capitalize()
    party.append(n)

while True:
    vibor = input('yes or no: ')
    if vibor == "yes":
        i = input(' imya ')
        party.append(i)
        continue
    elif vibor == "no":
        break
print(party)

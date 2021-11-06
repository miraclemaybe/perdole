Peredachi = []
for i in range(4):
    n = input("programs?")
    Peredachi.append(n)

prog2 = input('ezhe peredachu')
mesto = int(input('kuda postavim?'))
Peredachi.insert(mesto,prog2)
for i in Peredachi:
    print(i)
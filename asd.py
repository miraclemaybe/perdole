name = input("name?")
l = len(name)
if l < 5 :
    sirname = input("familiya?")
    print(sirname+name)
    c = name.upper()
    print(c)
elif l >= 5:
    v = name.lower()
    print(v)

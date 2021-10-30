bluda={}
for i in range(4):
    eda1=input('vvedi bluda:')
    bluda.update({i:eda1})
print(bluda)
sadeda=int(input('kakoe menshe nravirsa?'))
bluda.pop(sadeda)
print(bluda)
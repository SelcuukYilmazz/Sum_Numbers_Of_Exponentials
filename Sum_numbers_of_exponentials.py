import sys
k = []
goruntu = []
a = int(sys.argv[1])
b = int(sys.argv[2])
c = (a**b)
k.append(str(c))
toplam = 0
for l in k[0]:
    sayi = int(l)
    toplam += sayi
print(a,"^",b,"=",c,end=" = ")
item = str(c)
while 1:
    for s in item:
        goruntu.append(s)
    toplam = sum(map(int, goruntu))
    print("+".join(goruntu),end="")
    print(" =",toplam,end="")
    if toplam < 10:
        pass
    else:
        print(" = ",end="")
    item = str(toplam)
    if len(item) > 1:
        goruntu.clear()
        continue
    else:
        break

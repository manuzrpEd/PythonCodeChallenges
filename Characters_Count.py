Entrada_orig='F F F G X C Z Z Z Y Y X X X X D D D X X X F F F F'
Entrada=Entrada_orig.replace(" ","")
lst=[]

n=0
for i in range(len(Entrada)):
    if i==0:
        lst.append([Entrada[i]])
    else:
        if Entrada[i]!=Entrada[i-1]:
            lst.append([Entrada[i]])
            n=n+1
        else:
            lst[n].append(Entrada[i])

letters=[l[0] for l in lst]
count=[len(l) for l in lst]

print("Entrada :\n",Entrada_orig)
print("Salida :\n",letters,"\n",count)

# salida

# F G X C Z Y X D X F

# 3 1 1 1 3 2 4 3 3 4
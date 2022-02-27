a = '12'
b = '23'
print(a + b)

L = [[66, 12, 8], [1, 2, 3]]
print(L[0][1])

D = {'ali': 2, 'amir': 3}
print(D['amir'])

if L[0][1] == 9:
    print('ok')

if L[0][1] == 9:
    print('nine')
elif L[0][1] == 10:
    print('ten')
elif L[0][1] == 11:
    print('11')
elif L[0][1] == 12:
    pass
else:
    print('no')
L1 = [66, 12, 8]
for i in L:
    for j in i:
        print(i,j)
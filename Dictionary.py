D={1:'Name','Roll no.':2,'Div':'D'}
print(D)
print(D['Roll no.'])
print(D[1])
del (D['Roll no.'])
print(D)
D[4]='kmn'
print(D)
print(list(D))
print(list(D.values()))
print(list(D.items()))


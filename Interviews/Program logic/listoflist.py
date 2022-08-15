#list of list is present, fetch the sublist which has element of highest length

a = [['cucumber','raddish','pumpkin'],['apple','mango','banana'],['sparrow','myna','owl','ostrich']]

b = []

for j in a:
    c = max(j, key=len)
    b.append(c)
d = max(b, key=len)
for i in a:
    if d in i:
        print(i)










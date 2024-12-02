def inter(e1,e2):
    e =[]
    for i in e1:
        for k in e2:
            if i==k and i not in e:
                e.append(i)
                
    return e

e1=[1,2,2,3]
e2=[2,3,4]
print(inter(e1,e2))
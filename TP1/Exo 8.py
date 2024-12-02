def somme_varargs(*args):
    s=0
    for k in args:
        s+=k
    return s
print(somme_varargs(1,5,3,1))
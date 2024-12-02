def max_tuple(t):
    max = t[0]
    for element in t:
        if element > max :
            max = element
    return max

liste = [14,5,3,11,20,2]
print(max_tuple(liste))
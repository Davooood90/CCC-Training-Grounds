array3 = []
c1 = 0
c2 = 0
while True:
    if c1 >= len(array1) and c2 >= len(array2):
        break
    elif c1 >= len(array1):
        array3.append(array2[c2])
        c2 += 1
    elif c2 >= len(array2):
        array3.append(array1[c1])
        c1 += 1
    elif array1[c1] > array2[c2]:
        array3.append(array2[c2])
        c2 += 1
    elif array1[c1] < array2[c2]:
        array3.append(array1[c1])
        c1 += 1
    else:
        array3.append(array1[c1])
        c1 += 1
        array3.append(array2[c2])
        c2 += 1
    
x = int(len(array3)/2) - 1
if len(array3) % 2 == 0:
    y = ((array3[x] + array3[x + 1])/2)
    if y * 10 % 10 == 0:
        return int(y)
    return y
else:
    return int(array3[x + 1])

N = int(input())

table = []

for i in range(N):
    table.append(list(map(int, input().split())))

count = {
    "l": 0,
    "r": 0,
    "t": 0,
    "b": 0
}

table2 = []

for i in range(len(table)):
    if table[i] == sorted(table[i]):
        count["l"] += 1
    elif table[i] == sorted(table[i], reverse=True):
        count["r"] += 1

    temp = []
    for j in range(len(table)):
        temp.append(table[j][i])
    if temp == sorted(temp):
        count["t"] += 1
    elif temp == sorted(temp, reverse=True):
        count["b"] += 1
    table2.append(sorted(temp))

if count["l"] == N and count["t"] == N:
    for i in table:
        print(' '.join(list(map(str,i))))
elif count["r"] == N and count["t"] == N:
    for i in reversed(table2):
        print(' '.join(list(map(str, sorted(i)))))
elif count["r"] == N and count["b"] == N:
    for i in reversed(table):
        print(' '.join(list(map(str, sorted(i)))))
else:
    for i in table2:
        print(' '.join(list(map(str,i))))

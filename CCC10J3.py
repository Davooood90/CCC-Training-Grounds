num = {
    "A": 0,
    "B": 0
}

i = ""

while True:
    i = input()
    if i == "7":
        break
    i = i.split()
    if i[0] == "1":
        num[i[1]] = int(i[2])
    elif i[0] == "2":
        print(num[i[1]])
    elif i[0] == "3":
        num[i[1]] += num[i[2]]
    elif i[0] == "4":
        num[i[1]] *= num[i[2]]
    elif i[0] == "5":
        num[i[1]] -= num[i[2]]
    elif i[0] == "6":
        num[i[1]] = int(num[i[1]] / num[i[2]])

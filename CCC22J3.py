instruct = input()

pr = ""
for i in range(len(instruct)):
    if instruct[i].isalpha():
        pr += instruct[i]
    elif instruct[i] == "-":
        pr += " loosen "
    elif instruct[i] == "+":
        pr += f" tighten "
    else:
        pr += instruct[i]
        if i + 1 == len(instruct) or instruct[i+1].isalpha():
            print(pr)
            pr = ""

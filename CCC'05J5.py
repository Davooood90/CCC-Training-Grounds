while True:
    word = input()
    if word == "X":
        break

    while True:
        numa = word.count("ANA")
        numb = word.count("BAS")
        if numa > 0:
            word = word.replace("ANA", "A")
        if numb > 0:
            word = word.replace("BAS", "A")
        if numa == numb == 0:
            break
    
    if word == "A":
        print("YES")
    else:
        print("NO")



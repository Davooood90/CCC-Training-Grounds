M = int(input())
timetaken = [0]*101
responded = [0]*101
senttime = [0]*101
time = 0
for i in range(M):
    ss = input().split()
    cmd = ss[0]
    n = int(ss[1])
    if cmd == 'S':
        timetaken[n] += time - senttime[n]
        responded[n] = 1
    elif cmd == "R":
        responded[n] = -1
        senttime[n] = time
    else:
        time += n-2
    time += 1
for j in range(101):
    if responded[j] != 0:
        if responded[j] > 0:
            print(j, timetaken[j])
        else:
            print(j, responded[j])

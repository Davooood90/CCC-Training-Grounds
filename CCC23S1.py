C = int(input())

top = list(map(int, input().split()))
bottom = list(map(int, input().split()))

count = 0
beforet = 0
beforeb = 0

for i in range(C):
    if top[i] == 1:
        count += 3
        if beforet == 1:
            count -= 2
        beforet = 1
    else:
        beforet = 0
    
    if bottom[i] == 1:
        count += 3
        if i % 2 == 0 and top[i] == 1:
            count -= 2
        if beforeb == 1:
            count -= 2
        beforeb = 1
    else:
        beforeb = 0
        

print(count)


    

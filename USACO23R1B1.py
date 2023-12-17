N, M = map(int, input().split())

cow_height = list(map(int, input().split()))
can_height = list(map(int, input().split()))

for i in can_height:
    bot = 0
    for x, j in enumerate(cow_height):
        if bot <= j:
            cow_height[x] += min(j, i) - bot
            bot = min(j, i)
        if bot == i:
            break

for i in cow_height:
    print(i)

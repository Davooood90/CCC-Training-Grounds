trout_point = int(input())
pike_point = int(input())
pickerel_point = int(input())
limit = int(input())

answer = 0

for pickerel_num in range(limit // pickerel_point + 1):
    for pike_num in range(limit // pike_point + 1):
        for trout_num in range(limit // trout_point + 1):
            if trout_num == 0 and pike_num == 0 and pickerel_num == 0:
                continue
            if (trout_point * trout_num + pickerel_point * pickerel_num + pike_point * pike_num) <= limit:
                answer += 1
                print(f"{trout_num} Brown Trout, {pike_num} Northern Pike, {pickerel_num} Yellow Pickerel")

print(f"Number of ways to catch fish: {answer}")




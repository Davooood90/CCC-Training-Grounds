T = int(input())
G = int(input())

teams = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

games = [(1, 2), (1, 3), (1, 4), (2,3), (2,4), (3, 4)]

for i in range(G):
    game = input().split()
    games.remove((int(game[0]), int(game[1])))
    if int(game[2]) > int(game[3]):
        teams[int(game[0])] += 3
    elif int(game[2]) < int(game[3]):
        teams[int(game[1])] += 3
    else:
        teams[int(game[0])] += 1
        teams[int(game[1])] += 1

remain = len(games)

possible_values = ['W', 'L', 'T']
combinations = []
cind = [0] * remain

while True:
    current_combination = [possible_values[i] for i in cind]
    combinations.append(''.join(current_combination))
    
    for i in range(remain):
        cind[i] += 1
        if cind[i] == len(possible_values):
            cind[i] = 0
        else:
            break

    if cind == [0] * remain:
        break

cnt = 0

for combo in combinations:
    score = [teams[1], teams[2], teams[3], teams[4]]
    for i in range(len(combo)):
        if combo[i] == "W":
            score[games[i][0] - 1] += 3
        elif combo[i] == "L":
            score[games[i][1] - 1] += 3
        else:
            score[games[i][0] - 1] += 1
            score[games[i][1] - 1] += 1
    
    if score[T - 1] == max(score) and score.count(max(score)) == 1:
        cnt += 1


print(cnt)

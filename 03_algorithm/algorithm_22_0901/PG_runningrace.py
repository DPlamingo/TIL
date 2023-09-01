# 달리기 경주

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

for i in callings:
    cnt = players.index(i)
    players[cnt], players[cnt-1] = players[cnt-1], players[cnt]

print(players)
n, d = (int(x) for x in input().split())
snakes = []

for i in range(n):
    t, l = (int(x) for x in input().split())
    snakes.append([t, l])

for k in range(1, d+1):
    max_volume = 0
    
    for snake in snakes:
        max_volume = max(max_volume, snake[0]*(snake[1]+k))
    
    print(max_volume)
n = int(input())

tasks = []
for _ in range(n):
    a, d = map(int, input().split())
    tasks.append((a, d))

tasks.sort(key=lambda x: x[0])

total_reward = 0
current_time = 0

for a, d in tasks:
    current_time += a        
    reward = d - current_time  
    total_reward += reward

print(total_reward)
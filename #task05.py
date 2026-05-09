n = int(input())
tasks = []
for i in range(n):
    s, e = map(int, input().split())
    tasks.append((e, s))  # store as (end, start)

# Sort by end time; if end times are equal, pick latest start (shortest task)
tasks.sort(key=lambda x: (x[0], -x[1]))

selected = []
last_end = -1  # nothing selected yet

for e, s in tasks:
    if s > last_end:          # must start STRICTLY after previous task ends
        selected.append((s, e))
        last_end = e

print(len(selected))
for s, e in selected:
    print(s, e)
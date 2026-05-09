T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    
    tasks = []
    for i in range(n):
        s, e = map(int, input().split())
        tasks.append((e, s)) 
    
    tasks.sort(key=lambda x: (x[0], -x[1]))
    
    people = [-1] * m   
    count = 0
    for e, s in tasks:

        best = -1
        best_end = -2  
        
        for i in range(m):
            if people[i] < s:          
                if people[i] > best_end:  
                    best_end = people[i]
                    best = i
        
        if best != -1:
            people[best] = e 
            count += 1
    
    print(count)
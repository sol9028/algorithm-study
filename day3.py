lst = [0]*46

def trifunc(n):    
    for i in range(1, 46):
        for j in range(i, 46):
            for k in range(j, 46):
                if lst[i] + lst[j] + lst[k] == n:
                    return 1
    return 0

for i in range(1, 46):
    lst[i] = lst[i-1]+i

t = int(input())
for _ in range(t):
    n = int(input())
    print(trifunc(n))
a = list(map(int, input().split()))
m = int(input())
counter = 0
 
for x in a:
    if x == m:
        counter += 1
 
print(counter)
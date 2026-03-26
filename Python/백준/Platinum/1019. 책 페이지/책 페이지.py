n = int(input())
counts = [0] * 10
point = 1
start = 1

def calc(num, p):
    while num > 0:
        counts[num % 10] += p
        num //= 10

while start <= n:
    while n % 10 != 9 and start <= n:
        calc(n, point)
        n -= 1
        
    if start > n:
        break
        
    while start % 10 != 0 and start <= n:
        calc(start, point)
        start += 1
        
    start //= 10
    n //= 10
    
    for i in range(10):
        counts[i] += (n - start + 1) * point
        
    point *= 10

print(*counts)
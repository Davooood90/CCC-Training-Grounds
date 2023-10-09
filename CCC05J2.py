b = int(input())
e = int(input())

r = 0

for i in range(b, e + 1):
    c = 0
    for j in range(i):
        if i % (j + 1) == 0:
            c += 1
    if c == 4:
        r += 1

print(f"The number of RSA numbers between {b} and {e} is {r}")

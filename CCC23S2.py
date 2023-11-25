N = int(input())

mountains = list(map(int, input().split()))

values = [99999999999] * N

values[0] = 0

for i in range(N):
    prev_odd = 0
    for j in range(min(i, N-i-1)):
        prev_odd = abs(mountains[i - j - 1] - mountains[i + j + 1]) + prev_odd
        if prev_odd < values[(j + 1) * 2]:
            values[(j + 1) * 2] = prev_odd

    prev_even = 0
    if i < N - 1:
        for j in range(1, min(i, max(0, N-i-2)) + 2):
            prev_even = abs(mountains[i - (j - 1)] - mountains[i + j]) + prev_even
            if prev_even < values[(j * 2) - 1]:
                values[(j * 2) - 1] = prev_even

for i in values:
    print(i, end=" ")

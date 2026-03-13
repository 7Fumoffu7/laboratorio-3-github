import sys

input = sys.stdin.readline
MAX = 10_000_000

prime = bytearray(b'\x01') * (MAX + 1)
prime[0] = prime[1] = 0

limit = int(MAX ** 0.5) + 1

for i in range(2, limit):
    if prime[i]:
        prime[i*i:MAX+1:i] = b'\x00' * ((MAX - i*i)//i + 1)
#comentando para el commit
pref = [0] * (MAX + 1)
count = 0
for i in range(MAX + 1):
    if prime[i]:
        count += 1
    pref[i] = count
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a < 1:
        a = 1
    print(pref[b] - pref[a - 1])
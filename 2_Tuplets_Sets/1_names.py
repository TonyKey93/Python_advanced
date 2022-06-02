n = int(input())
a = list()
for _ in range(n):
    a.append(input())

a = set(a)
a = list(a)
for i in range(len(a)):
    print(a[i])

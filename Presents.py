n = int(input())
a = [int(i) for i in input().split()]
ans = [0]*n
for index, value in enumerate(a):
    ans[index] = a.index(index+1)+1

for j in ans:
    print(j, end=' ')

n = int(input("최대 몇개를 찍을까여? "))
for i in range(1, n+1):
    print(' '*(n-i)+'*'*i)
for i in range(1, n):
    print(' '*i+'*'*(n-i))

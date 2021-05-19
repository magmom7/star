n = int(input("최대 몇개를 찍을까여? "))
for i in range(1, n+1):
    print(' '*(n-i)+'*'*i+'*'*(i-1))
for i in range(1, n):
    print(' '*i+'*'*(n-i)+'*'*(n-1-i)+' '*i)

'''
url = https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

'''
n = int(input())
s = set(map(int, input().split()))

for i in range(n):
    cmd = list(input().split(' '))
    if (len(cmd) == 1):
        s.pop()
    else:
        value = int(cmd[1])
        s.discard(value)
print(sum(s))

'''
url = https://www.hackerrank.com/challenges/list-comprehensions/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n])

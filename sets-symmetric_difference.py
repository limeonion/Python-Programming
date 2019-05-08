'''
url = https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
'''

a = input()
list_eng = set(map(int, input().split()))

b = input()
list_fre = set(map(int, input().split()))

print(len(list_eng ^ list_fre))


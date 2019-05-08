'''
url = https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''



n = input()
list_eng = set(map(int, input().split()))

b = input()
list_fre = set(map(int, input().split()))

print(len(list_eng.intersection(list_fre)))

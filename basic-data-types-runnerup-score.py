'''
url = https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
'''
n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])

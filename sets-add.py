'''
f we want to add a single element to an existing set, we can use the .add() operation. 
It adds the element to the set and returns 'None'.

Example

>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])

The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from. 


Output Format

Output the total number of distinct country stamps on a single line.

'''
n = int(input())
countries = set()

for i in range(n):
    countries.add(input())
print(len(countries))

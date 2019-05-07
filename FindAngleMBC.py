import math
ab = float(input())
bc = float(input())
ac = math.sqrt((ab*ab)+(bc*bc))
bm = ac / 2.0
mc = bm
#let, 
b = mc
c = bm
a = bc
#where b=c
b_radian = math.acos(a / (2*b))
b_degree = int(round((180 * b_radian) / math.pi))
output_str = str(b_degree)+'°'
print(output_str)

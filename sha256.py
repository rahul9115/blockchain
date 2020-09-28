import math
s=math.sqrt(3)
print(s)
print(math.modf(s))
f=math.modf(s)[0]
fp=f*math.pow(2,32)
print(fp)
print(hex(int(fp)))


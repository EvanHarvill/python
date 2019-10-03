# bincon.py cwc
n = int(input("Input an integer less than 256 : "))
# d(dividend) q(quotient) r(remainder)
d = 128
q = int(n / d)
r = n % d
n = q
print(q,r)
# - - - -
d = d / 2
q = int(n / d)
r = n % d
print(q,r)

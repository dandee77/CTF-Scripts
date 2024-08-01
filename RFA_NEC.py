from Crypto.Util.number import inverse, long_to_bytes

n = 0 #given
e = 0 #given, modulos inverse of d
c = 0 #given
#first you need to factor n at factordb.com (ex. 23 * 1199919)
p = 0 #replace w/ factored N1
q = 0 #replace w/ factored N2

phi = (p - 1) * (q - 1)
d = inverse(e, phi)

m = pow(c, d, n)
print(long_to_bytes(m))
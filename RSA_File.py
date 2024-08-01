import json
import math
from Crypto.Util.number import long_to_bytes


data = json.load(open('data.txt').read())

for i, x in enumerate(data):
    for j, y in enumerate(data):

        if i == j:
            continue

        P = math.gcd(x["N"], y["N"])

        if P > 1:
            Q = x["N"] // P
            phi_N = (P - 1) * (Q - 1)
            D = pow(65537, -1, phi_N)

            PT = pow(x["Flag"], D, x["N"])
            print(long_to_bytes(PT))
            exit()





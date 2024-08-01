from Crypto.Util.number import long_to_bytes

N = "idk"
E = 3
Flag = 1191166778589221327 # Replace with the actual flag

def cube_root(N):

    low = 0
    mid = N // 2
    high = N

    while low < mid < high:
        if mid ** 3 > N:
            high = mid - 1
        elif mid ** 3 < N:
            low = mid + 1

        mid = low + ((high - low) // 2)
        return mid
    
print(long_to_bytes(cube_root(Flag)))
def addOne(x) :

    m = 1;

    # until we find a 0
    while x & m:
        # Flip all the set bits
        x = x ^ m
        m = m << 1

    x = x ^ m

    return x
# Driver program
n = 13
print addOne(n)

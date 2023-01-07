def fast_pow(x, k, P):
    re = 1
    while k:
        if k & 1:
            re = re * x % P
        x = x * x % P
        k >>= 1
    return re
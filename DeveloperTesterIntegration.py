def formTeam(d, t, q):
    dpD = [0 for _ in range(q + 1)]
    dpT = [0 for _ in range(q + 1)]
    dpD[0] = dpD[1] = 1
    dpT[0] = dpT[1] = 1
    mod = 10**9 + 7
    for i in range(2, q+1):
        if i < d:
            dpD[i] = (dpD[i-1] + dpT[i-1]) % mod
        else:
            dpD[i] = (dpD[i-1] + dpT[i-1] - dpT[i-d]) % mod
        if i < t: 
            dpT[i] = (dpT[i-1] + dpD[i-1]) % mod
        else:
            dpT[i] = (dpD[i-1] + dpT[i-1] - dpD[i-d]) % mod
    return (dpD[-1] + dpT[-1]) % mod

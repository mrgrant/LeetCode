from functools import lru_cache
from itertools import groupby
@lru_cache()
def candyCrush1D_followup(S):
    l, segs = 0, []
    for c, seq in groupby(S):
        k = len(list(seq))
        if k >= 3:
            segs.append((l, l + k))
        l += k
    return min([
        candyCrush1D_followup(S[:l] + S[r:]) 
        for l, r in segs
    ], key=len, default=S)
        

S = "aaabbbacd"
print(candyCrush1D_followup(S))
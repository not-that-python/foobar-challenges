def solution(pegs):
    difs = [pegs[i+1] - pegs[i] for i in range(len(pegs) - 1)]
    a = 0
    for i in range(len(difs)):
        if i%2 != 0:
            a -= difs[i]
        else:
            a += difs[i]
    A = 2*a
    if a<1:
        return[-1, -1]
    if len(pegs) % 2!= 0:
        b = 1
    else:
        
        r0=A/3
        
        rs=[r0]*len(pegs)
        
        for i in range(len(difs)):
            rs[i+1] = difs[i] - rs[i]
        for i in rs:
            if i <= 0:
                return[-1, -1]
        
        if A%3 == 0:
            A /= 3
            b = 1
        else:
            b = 3
        
    return [A, b]

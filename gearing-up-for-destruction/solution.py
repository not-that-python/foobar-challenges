def solution(pegs):
    difs = [pegs[i+1] - pegs[i] for i in range(len(pegs) - 1)] # The differences in length between each peg
    a = 0
    for i in range(len(difs)):
        if i%2 != 0:
            a -= difs[i]
        else:
            a += difs[i]
        # Finds the radius of the last cog
    a_2 = 2*a
    if a<1:
        return [-1, -1]
    # Not possible if the radius ends up being negative
    if len(pegs) % 2!= 0:
        b = 1
        # If the number of pegs is even, the denominator is 1
    else:
        
        r0=a_2/3 # Radius of the first cog
        
        rs=[r0]*len(pegs)
        
        for i in range(len(difs)):
            rs[i+1] = difs[i] - rs[i]
            # Makes a list (rs) of the radii of every cog
        for i in rs:
            if i <= 0:
                return[-1, -1]
            # Not possible if the radii of any of the cogs are negative
        
        if a_2%3 == 0:
            a_2 /= 3
            b = 1
            # If a_2 is divisible by 3, divide a_2 by 3 and make the denominator 1 to simplify the fraction
        else:
            b = 3
            # Otherwise make the denimonator 3 and keep a_2 the same, as it's now in its simplest form
        
    return [a_2, b]

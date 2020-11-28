def solution(xs):
    
    if len(xs) == 1:
        return str(xs[0])
    
    if any(i<0 for i in xs):
        negs = [i for i in xs if i < 0]
        if len(negs) % 2 != 0:
            xs.remove(max(negs))
    
    if any(i==0 for i in xs):
        xs = [i for i in xs if i != 0]
    
    result = 1
    for i in xs:
        result *= i
    if len(xs) == 0:
        return '0'
    else:
        return str(result)

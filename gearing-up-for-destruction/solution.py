def solution(pegs):
    len_pegs = len(pegs)
    dist=[pegs[i+1]-pegs[i] for i in range(len_pegs-1)]
    
    rn=0
    for i in range(len_pegs-1):
        if i%2==0:
            rn+=dist[i]
        else:
            rn-=dist[i]
    r0=2*rn
       
    if rn <= 1:
        return [-1,-1]
    
    if len_pegs%2==0:
        if r0/3>=dist[0]-1:
            return[-1,-1]
        if rn/3>=dist[-1]-1:
            return[-1,-1]
        
        a=int(r0/3)   
        rs=[a]*len_pegs
        for i in range(len_pegs-1):
            rs[i+1]=dist[i]-rs[i]
            
        for q in rs:
            if q<=0:
                return[-1,-1]
                
        if r0%3==0:
            r0=int(r0/3)
            dr=1
        else:
            dr=3
        
    else:
        if r0>=dist[0]-1:
            return[-1,-1]
        if rn>=dist[-1]-1:
            return[-1,-1]  
        dr=1
    
    return[r0,dr]

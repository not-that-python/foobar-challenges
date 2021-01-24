def solution(xs):
    
    if len(xs) == 1:
        return str(xs[0])
    # This returns the first element in xs if there's only 1 element in xs.
    
    if any(i<0 for i in xs): # Checks for any negative numbers in xs
        negs = [i for i in xs if i < 0]
        if len(negs) % 2 != 0: # Checks if the number of negative numbers are even or not (since an even number of negatives multiplied together is positive.)
            xs.remove(max(negs))
            # If it isn't even, remove the negative value closets to 0 - the one with the least effect on the multiplication.
    
    if any(i==0 for i in xs):
        xs = [i for i in xs if i != 0]
        # Removes all the 0s from xs
    
    
    if len(xs) == 0:
        return '0'
    # If after the removal, there aren't any numbers left, return 0
    else:
        result = 1
        for i in xs:
            result *= i
            # Goes through the multiplication
        return str(result)

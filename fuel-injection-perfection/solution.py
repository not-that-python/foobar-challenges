def solution(n):
    n = int(n) # Makes n an integer
    count = 0
    while n != 1:
        if n % 2 != 0:
            # If n is odd...
            n = (n - 1 if n % 4 == 1 or n == 3 else n + 1)
            # Take one away from n if n - 1 is divisible by 4 or if n is 3. Otherwise, add one to n.
            count += 1
        n /= 2 # Keep halving n until it reaches 1
        count += 1
    return count

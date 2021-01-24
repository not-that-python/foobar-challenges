def solution(data, n):
    new_data = [i for i in data if data.count(i) <= n]
    # This makes a new list out of data called 'new_data', which checks all the elements in data if the number of the same element within is less than n.
    return new_data

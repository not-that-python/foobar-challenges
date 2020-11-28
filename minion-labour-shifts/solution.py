def solution(data, n):
    new_data = [i for i in data if data.count(i) <= n]
    return new_data

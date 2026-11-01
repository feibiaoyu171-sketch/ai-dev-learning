def filter_positive(nums):
    s = []
    for i in nums:
        if i > 0:
            s.append(i)
    return  s

print(filter_positive([-1,-2,1,3,0,-5]))

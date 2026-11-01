def sum_even(nums):
    total= 0
    for num in nums:
        if num % 2 == 0 :
            total += num
    return total
nums = [1,2,3,4,5,6,7,8,9,0]
print(sum_even(nums))
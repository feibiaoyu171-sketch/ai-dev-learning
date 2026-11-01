def max_min_diff(nums):
    max_num = max(nums)
    min_num = min(nums)
    return max_num,min_num
nums = [1,2,3,4,5,0,6]
max_num,min_num = max_min_diff(nums)
print(f"最大值为：{max_num},最小值为：{min_num}。")
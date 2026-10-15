def count_items(nums):
    if nums == []:
        return 0
    return 1 + count_items(nums[1:])

print(count_items([2,4,3,56,33,54,34,]))

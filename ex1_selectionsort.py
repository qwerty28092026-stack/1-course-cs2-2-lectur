
def selection_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        max_i = i

        for j in range(i + 1, n):
            if nums[j] > nums[max_i]:
                max_i = j

        nums[i], nums[max_i] = nums[max_i], nums[i]

    return nums


grades = [4, 2, 5, 3, 5, 4, 3]

print("По убыванию:", selection_sort(grades.copy()))

def cycle_sort(nums):
    for i in range(0, len(nums)):
        while rank(nums, nums[i]) != i:
            d = rank(nums, nums[i])
            nums[i], nums[d] = nums[d], nums[i]


def rank(nums, x):
    rank = 0
    for i in range(0, len(nums)):
        if nums[i] < x:
            rank += 1
    return rank


if __name__ == "__main__":
    nums = [3, 1, 5, 15, 11, 13, 9, 7, 17, 19, 21]
    cycle_sort(nums)

    print(nums)

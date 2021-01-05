# LC 448 in array 1<=a[i]<=n some elements appear twice some once
# find all elements [1,n] that don't appear in array

def f(nums):
    # ideal input for cycle sort 1,2,3,4,5,6,7,8
    #                           0 1 2 3 4 5 6 7

    for i in range(0, len(nums)):
        while nums[i] != (i + 1):
            d = nums[i] - 1
            # sanity check if position doesn't have duplicate
            if nums[d] != nums[i]:
                # swap
                nums[i], nums[d] = nums[d], nums[i]
            else:
                break
    res = []
    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)

    return res


if __name__ == "__main__":
    # output [5,6]
    print(f([4, 3, 2, 7, 8, 2, 3, 1]))

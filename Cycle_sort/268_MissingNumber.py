# LC 268 array of n numbers from 0 to n. Return the only number which is missing from array

def missing_number(nums):
    # iterate through array
    for i in range(0, len(nums)):

        # while number is not at correct position
        while nums[i] != i:
            # d - destination index where it should be placed
            d = nums[i]
            # sanity check, if passed then elements are swapped if not element stays at incorrect position
            # element at incorrect position will be the answer
            if d != len(nums):
                nums[i], nums[d] = nums[d], nums[i]
            else:
                break
    # scan for element not in correct position, this is is the answer
    for i in range(0, len(nums)):
        if i != nums[i]:
            return i

    return len(nums)


if __name__ == "__main__":
    print(missing_number([0, 1, 3]))
    print(missing_number([0]))

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # in order to get the window range, need the start and last number in the list
    window = []
    start = 0
    last = start + (k - 1)
    # while loop, can't be more that length of arr
    while last != len(nums):
        current = nums[start]  # setting current
        for i in range(start, last + 1):  # iterate through the next window
            if nums[i] > current:
                current = nums[i]  # new current max
        window.append(current)
        start += 1
        last += 1
    return window


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

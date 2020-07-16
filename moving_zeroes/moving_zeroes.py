'''
Input: a List of integers
Returns: a List of integers
'''

'''
    - for/while loop
    - remove the zeros
    - need to keep count of arr length
    - return the list
'''


def moving_zeroes(arr):
    # first try
    # arr = [num for num in arr if num != 0]
    # return len(arr)

    cur = 0
    count = 1
    while count <= len(arr):
        if arr[cur] == 0:
            cur_num = arr.pop(cur)
            arr.append(cur_num)
        else:
            cur += 1
        count += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

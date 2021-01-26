'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # using naive method
    # res = []
    # for num in arr:
    #     if num not in res:
    #         res.append(num)
    # return res

    # return list(set(arr))

    # result = set()
    # for elem in arr:
    #     if elem not in arr:
    #         result.add(elem)

    res = []
    for num in arr:
        if num in res:
            res.remove(num)
        elif num not in res:
            res.append(num)
    return res[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

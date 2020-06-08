'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# implement a solution that finds the single number in _one_ pass through the input array with `O(1)` space complexity?

def single_number(arr):
    # Your code here
    cur = 0
    found = 0
    # if the two first elements are not the same.. then the list needs to be sorted
    if arr[0] != arr[1]:
        arr.sort()

    # while cur pointer is not the length of the array passed in... walk
    while cur != len(arr) :
        # print(f'checking... {arr[cur]} {arr[cur+1]}')

        if arr[cur] == arr[cur + 1]:
            pass
        else:
            found = cur
            cur += 1

        # update the cur pointer before the next iteration
        cur += 2


    return arr[found]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
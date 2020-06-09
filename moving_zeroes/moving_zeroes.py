'''
Input: a List of integers
Returns: a List of integers

Write a function that takes an array of integers and
moves each non-zero integer to the left side of the array,
then returns the altered array. 

The order of the non-zero integers does not matter in the mutated array.

'''

# Your code here


def moving_zeroes(arr):  # O(n)
    # pointers to the start and beginning of the list
    left = 0
    right = len(arr)-1

    # while the pointers dont match. contine to see if 
    # items in the list neeed to be swapped
    while left != right :
        # if the value of the left side is not 0 then
        # it is okay to continue
        if arr[left] != 0:
            # add one to the left side --> move the pointer
            left += 1
        # else if the value is a zero [0, ...]
        # then it needs to be swapped
        elif arr[left] == 0 :
            # save the value 
            prev = arr[right]
            # replace the value at the end of the list
            # with the value at the left pointer
            arr[right] = arr[left]
            # replace the value at the left pointer
            # with the prev value
            arr[left] = prev
            # move the right pointer <-- to the left one
            right -= 1

    
    # once the iterations have finished the array will be sorted
    # so return it
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

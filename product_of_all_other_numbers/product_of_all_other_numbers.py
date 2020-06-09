'''
Input: a List of integers
Returns: a List of integers
'''

# UNDERSTAND

#  -- The function will take in an list of any given length
#  -- with each item in the list (n)
#  -- multiply it by each other item

# --- GIVEN [1,7,9,8,6,5,4]
# --- () => represents a single pass through the while loop
# --- {__n__} => current value
# --- [
# ---  (((((( {__1__} * 7) * 8) * 9) * 6) * 5) * 4)
# ---  (((((( {__7__} * 1) * 8) * 9) * 6) * 5) * 4)
# ---  (((((( {__8__} * 1) * 7) * 9) * 6) * 5) * 4)
# ---  (((((( {__9__} * 1) * 7) * 8) * 6) * 5) * 4)
# ---  (((((( {__6__} * 1) * 7) * 8) * 9) * 5) * 4)
# ---  (((((( {__5__} * 1) * 7) * 8) * 9) * 6) * 4)
# ---  (((((( {__4__} * 1) * 7) * 8) * 9) * 6) * 5)
# --- ]

# PLAN
# -- I'm going to have to track the index I'm looking at currently
# -- I'm going to have to track the product of all numbers not current at this index

# EXECUTE


def product_of_all_other_numbers(arr):
    # if the length of the array is less than 2 then just return the array...
    # because an array of length 1 is already sorted
    copy = [x for x in arr]
    if len(arr) < 2:
        return arr
    # if the length of the array is of length 2. then the values in the array
    # require no math. just swap them.
    elif len(arr) == 2:
        arr[0], arr[1] = arr[1], arr[0]
    # the length is at least 3 so we can do something like [(b*c),(a*c), (a*b)]
    # given an array [1, 2, 4]
    else:
        # each index needs to be the product of each other index...
        # [1,2,3]
        # [(2*3),(1*3), (1*2)] => [6, 3, 2]
        # save the current index
        # pass it to the next
        # save the next index
        # repeat

        def product(ind, _arr):
            __p = 1
            for i in range(len(_arr)):
                if i != ind:
                    __p *= _arr[i]
            return __p

        for ind in range(len(arr)):
            arr[ind] = product(ind, copy)


        pass

    return arr

# REFLECT


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

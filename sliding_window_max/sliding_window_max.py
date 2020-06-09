'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

# UNDERSTAND
# --      v {start} v {start + k}
# --  [ [ _ ,    _ ,   _ , ] _ , _ , _ ]


def sliding_window_max(nums, k):
    # Your code here
    # current pointer
    # the beginning of the sliding window
    cur = 0
    # end of the sliding window
    end = cur + k
    # create a new array to return
    new_arr = []

    # helper function to fin the max of thw slider_window

    def find_max(slider_window): # O(n)
        # maximum value found in the slider
        max_value = slider_window[0] #O(1)

        # traverse the list and see if the current value is greater or less than the next value -->
        for ind in range(len(slider_window)):  # O(n)
            # if [a] >= max_value 
            # if the current value we are looking at inside the slider is
            # greater than the maximum value we have stored so far.. 
            if slider_window[ind] >= max_value: 
                # replacce the maximum value with the current value we are looking at.
                max_value = slider_window[ind]
                # continue until the end of the slider window

        return max_value

    # start the slider window
    # and run until the current value(start of the window) has looped until
    # it is at the maximum amount of slides
    # slides = l-k+1
    while cur != len(nums)-k+1:  # 8 -1 -3 => 4
        # sliding window debug function
        # print(f'\033[1;32;10m > {cur} -> {end} : \033[1;33;10m {origin[cur:end]} \033[1;31;0m \n')

        # add the maximum value found inside the nums between the start and end of the window.
        # to the new array to be returned
        new_arr.append(find_max(nums[cur:end]))

        # update the window to move --> 1 to the right
        cur += 1
        end += 1
        # repeat until slides are not allowed

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

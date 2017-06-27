# The maximum sum subarray problem consists in finding the maximum sum of
# a contiguous subsequence in an array or list of integers:

# maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]


def maxSequence(arr):
    if arr == []:
        return 0
    max_so_far = 0
    max_ending_here = 0
    for i in arr:
        max_ending_here = max_ending_here + i
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    print(max_so_far)

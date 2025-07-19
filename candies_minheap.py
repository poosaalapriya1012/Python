import heapq
'''Krishna loves candies a lot, so whenever he gets them, he stores them in boxes so he can eat them later. He has recently received N boxes of candies, each containing Ci candies. Krishna wants to store all the candies in a single box.
However, he can only merge two boxes at a time. The cost (time) to merge two boxes containing X and Y candies is X + Y seconds. The result of merging goes into a new empty box. Assume an infinite number of empty boxes are available.
Help Krishna determine the minimum total time required to merge all candy boxes into one.'''
def min_merge_time(arr):
    heapq.heapify(arr)
    total = 0
    while len(arr) > 1:
        x = heapq.heappop(arr)
        y = heapq.heappop(arr)
        merge = x + y
        total += merge
        heapq.heappush(arr, merge)
    return total
n = int(input("Enter number of boxes: "))
arr = list(map(int, input("Enter candies in each box: ").split()))
print("Minimum time to merge all boxes:", min_merge_time(arr))

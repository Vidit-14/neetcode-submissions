class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2  #eg. A = [1,2,3,4,5] , B = [1,2,3,4,5,6,7,8]
        total_len = len(nums1) + len(nums2)  #total = 5 + 8 = 13
        half = total_len // 2  #half = 6

        if len(B) < len(A):
            A, B = B, A  #we want A to be the smaller array for simplicity
        
        #running binary search on A
        l, r = 0, len(A) - 1
        while True:
            mid = (l + r) // 2    #elements to the left of median (from A)
            #mid = 2                [1,2,3] = left partition of A
            j = half - mid - 2    #elements to the left of median (from B)
            #j = 2                  [1,2,3] = left partition of B

            Aleft = A[mid]      if mid >= 0 else float('-inf')             #Aleft = 3  i.e rightmost element of left partition
            Aright = A[mid + 1] if (mid + 1) < len(A) else float('inf')    #Aright = 4 i.e leftmost element of right partition
            Bleft = B[j]        if j >= 0 else float('-inf')               #Bleft = 3
            Bright = B[j + 1]   if (j + 1) < len(B) else float('inf')      #Bright = 4

            if Aleft <= Bright and Bleft <= Aright:
                #this means partition is correct

                if total_len % 2:
                    #if len is odd -> only one median
                    return min(Aright, Bright)

                #if len is even -> median = avg of middle elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid - 1   #reduce len of left partition of A
            else:
                l = mid + 1
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        lo, hi = 0, m 
        while lo <= hi:
            i = (lo + hi) // 2 # number of elements in the left of A
            j = half - i  # number of elements in the left of B
            
            if i > 0 and j < n and A[i-1] > B[j]:
                # We included an element from A that is too large, and it belongs to the right partition of A
                hi = i - 1
            elif j > 0 and i < m and B[j-1] > A[i]:
                # Similarly, the partition of A is too small, need to move right.
                lo = i + 1
            else:
                # found the midpoint
                break
        
        if i == m:
            right = B[j]
        elif j == n:
            right = A[i]
        else:
            right = min(A[i], B[j])     
                
        if total % 2: # odd number of elements.
            return right
        
        # largest element on the left
        if i == 0:
            left = B[j-1]
        elif j == 0:
            left = A[i-1]
        else:
            left = max(A[i-1], B[j-1])

        return (left + right) / 2 # even number of elements, average of the two.


            
        
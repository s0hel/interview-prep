# https://www.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

# Given two unsorted arrays arr1[]  and arr2[], the task is to find all pairs whose sum equals x from both arrays.
#
# Note: All pairs should be returned in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then (u1,v1) should be returned first else second.


class Solution:
    def allPairs(self, x, arr1, arr2):
        result = []
        s1 = set(arr1)
        for n in arr2:
            diff = x - n
            if diff in s1:
                result.append([diff, n])

        result.sort(key=lambda pair: pair[0])
        return result


s = Solution()
print(s.allPairs(x=9, arr1=[1, 2, 4, 5, 7], arr2=[5, 6, 3, 4, 8]))

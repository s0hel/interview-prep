import random

# 278. First Bad Version
# Easy

# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check. Since
# each version is developed based on the previous version, all the versions after a
# bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version is bad.
# Implement a function to find the first bad version. You should minimize the number of calls to the API.
#
# Example 1:
#
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
# Example 2:
#
# Input: n = 1, bad = 1
# Output: 1
#
#
# Constraints:
#
# 1 <= bad <= n <= 231 - 1

bad_version = random.randint(1, 230)
num_versions = random.randint(bad_version, 230)

print(f"bad version: {bad_version}")
print(f"number of versions: {num_versions}")


def isBadVersion(version: int) -> bool:
    print(f"isBadVersion({version})")
    return version >= bad_version


class Solution:

    def first_bad_version(self, n: int) -> int:
        low = 1
        high = n
        #min_bad_version = n

        while low <= high:
            mid = ((high - low) // 2) + low
            print(f"mid = ((high({high}) - low({low}) // 2) + low({low})")

            if isBadVersion(mid):
                # below code is unnecessary, you can simply return 'low'
                #if mid < min_bad_version:
                #    min_bad_version = mid
                high = mid - 1
            else:
                low = mid + 1

        return low


s = Solution()

print(f"First bad version {s.first_bad_version(num_versions)}")

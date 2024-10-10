# 139. Word Break
# Medium
#
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented
# into a space-separated sequence of one or more dictionary words.
#
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#
#
#
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            if word in s:
                s = s.replace(word, '')

        return len(s) == 0

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:

        subsets = []

        # get all subsets of wordDict
        def get_subset(subset, index):
            if index == len(wordDict):
                subsets.append(subset.copy())
                return

            subset.append(wordDict[index])
            get_subset(subset, index + 1)

            subset.pop()
            get_subset(subset, index + 1)

        get_subset([], 0)

        def helper(s: str, wordSet: List[str]):
            for word in wordSet:
                if word in s:
                    s = s.replace(word, ' ' * len(word))

            return len(s.replace(' ', '')) == 0

        for subset in subsets:
            if helper(s, subset):
                return True

        return False

    def wordBreak3(self, s: str, wordDict: List[str]):
        cache = [False] * (len(s) + 1)
        cache[len(s)] = True

        i = len(s) - 1
        while i >= 0:
            for word in wordDict:
                if i + len(word) <= len(s) and s[i: i + len(word)] == word:
                    cache[i] = cache[i + len(word)]
                if cache[i]:
                    break
            i -= 1

        return cache[0]

s = Solution()

print(s.wordBreak3(s="ccaccc", wordDict=["cc", "ac"]))
print(s.wordBreak3(s="cbca", wordDict=["bc", "ca"]))
print(s.wordBreak3(s="cars", wordDict=["car", "ca", "rs"]))
print(s.wordBreak3(s="leetcode", wordDict=["leet", "code"]))
print(s.wordBreak3(s="applepenapple", wordDict=["apple", "pen"]))
print(s.wordBreak3(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))

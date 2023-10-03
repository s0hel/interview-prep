# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns three possible results:
#
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
#
#
#
# Example 1:
#
# Input: n = 10, pick = 6
# Output: 6
import random

# Example 2:
#
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
#
# Input: n = 2, pick = 1
# Output: 1

num = 10
pick = random.randint(1, num)

print(f"picked number: {pick}")


def guess_number(n: int) -> int:
    low = 1
    high = n

    while low <= high:
        mid = low + ((high - low) // 2)
        r = guess(mid)

        if r == 0:
            return mid
        elif r < 0:
            high = mid - 1
        else:
            low = mid + 1


def guess(guess_num: int) -> int:
    if guess_num > pick:
        return -1
    elif guess_num < pick:
        return 1

    return 0


result = guess_number(num)
print(f"Guessed Number: {result}")
from typing import List


class Solution:
    def getBitMask(self, word: str) -> int:
        mask = 0
        for c in word:
            i = ord(c) - ord('a')
            mask |= 1 << i
        return mask

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        letters = {}
        for word in words:
            mask = self.getBitMask(word)
            letters[mask] = letters.get(mask, 0) + 1
        solution = [0] * len(puzzles)

        for i in range(len(puzzles)):
            puzzle = puzzles[i]
            mask = self.getBitMask(puzzle)
            tmp_mask = mask
            total = 0
            first_bit_index = ord(puzzle[0]) - ord('a')

            while tmp_mask != 0:
                if tmp_mask >> first_bit_index & 1:
                    total += letters.get(tmp_mask, 0)
                tmp_mask = (tmp_mask - 1) & mask
            solution[i] = total

        return solution


s = Solution()
print(s.findNumOfValidWords(["aaaa", "asas", "able", "ability", "actt", "actor", "access"],
                            ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"]))
print(s.findNumOfValidWords(["apple", "pleas", "please"], ["aelwxyz", "aelpxyz", "aelpsxy", "saelpxy", "xaelpsy"]))

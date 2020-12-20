class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # recursive
        map_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # terminator
        if not digits:
            return ['']

        # process && drill down
        return list(c+d for c in self.letterCombinations(digits[:-1]) for d in map_dict[digits[-1]])

## fail with: "" -> [], but output [""] 

## 12/20/2020 使用递归解决。

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # recursive
        map_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        # terminator
        if not digits:
            return []
        if len(digits) == 1: # change terminator from level 0 to leval 1 technically.
            return list(map_dict[digits])

        # process && drill down
        return list(c+d for c in self.letterCombinations(digits[:-1]) for d in map_dict[digits[-1]])
from typing import List


class Solution:
    """
    This solution strictly follow the recursion template
    """

    # initiate with a result to store
    def __init__(self):
        self.res = []
        self.letter_map = {
            0: " ",
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.res
        self._letter_combo(0, len(digits), digits, "")
        return self.res

    def _letter_combo(self, curr_level, max_level, digits, curr_str):
        """

        :param curr_level: current digit
        :param max_level: length of the digits
        :param digits: digits
        :param curr_str: current letter string
        :return:
        """
        # terminator
        if curr_level >= max_level:
            self.res.append(curr_str)
            return

        # process the current logic
        # get the current digit
        digit = digits[curr_level]
        # make sure the digit is valid
        assert (0 <= int(digit) <= 9) and (int(digit) != 1)

        # get the letters of the digit
        letters = self.letter_map[int(digit)]

        # drill down for each letter
        for letter in letters:
            self._letter_combo(curr_level + 1, max_level, digits,
                               curr_str + letter)
        return


def test():
    sol = Solution()
    res = sol.letterCombinations("567")
    print(res)


if __name__ == '__main__':
    test()

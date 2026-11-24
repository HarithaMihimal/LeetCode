
class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = 0

        while x != 0:
            digit = x % 10 if x > 0 else -(abs(x) % 10)
            x = int(x / 10)

            # Check overflow
            if reversed_num > 214748364 or (
                reversed_num == 214748364 and digit > 7
            ):
                return 0

            # Check underflow
            if reversed_num < -214748364 or (
                reversed_num == -214748364 and digit < -8
            ):
                return 0

            reversed_num = reversed_num * 10 + digit

        return reversed_num

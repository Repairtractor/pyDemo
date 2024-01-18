# 字符串转换为整数，遇到-号为负，遇到其他字符停止
# 遇到-号，记为负数，
class Solution:
    def myAtoi(self, s: str) -> int:
        # 循环一次，确定正负
        is_negative = None
        flag = False
        res = 0
        # 临界值
        max_num = 2**31 // 10  # 这里如果是java的话，2的31次方就是负数，只需要转成正数，然后减一就好
        tail_num = 2**31 % 10

        for item in s:
            if item == " ":
                continue
            if (item == "-" or item == "+") and is_negative == None:
                is_negative = item == "-"
                continue
            if item.isdigit() != True:
                break
            # 这里需要处理溢出
            temp = int(item)
            # 如果已经大于前面的位数，或者等于并且与最后一位相等说明溢出了
            if res > max_num or (
                res == max_num and (temp >= tail_num if is_negative else tail_num - 1)
            ):
                return -(2**31) if is_negative else 2**31 - 1
            res = res * 10 + int(item)

        return -res if is_negative else res


cc = Solution().myAtoi("  -42")
print(cc)

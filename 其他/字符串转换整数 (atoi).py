# 首先需要理解题目的问题，给定一个字符串，过滤空格和第一个+/-，数字开始，遇到任何其他字母停止，那么就必然需要有一个标识来记录是否开始了数字，+、-号，
# 一旦已经出现过，后面的非数字类型统一结束掉，这里同样要注意溢出的情况处理，其实这道题本身就是需要处理两个问题，一个就是提取数字，第二个就是判断数字是否溢出
# 解：首先是提取数字，使用一个字段is_negative标识开头的字符，
    #1. 如果第一个有效字符是数字或者+,is_negative=false，
    #2.如果是-，is_negative=true，
    #3.当前面已经进行过有效数字时 空格算无效字符，直接结束，如果为None说明都是空格，继续过滤
#ok，根据上面的解释就可以获取到数字了

class Solution:
    def myAtoi(self, s: str) -> int:
        # 循环一次，确定正负
        is_negative = None
        res = 0
        # 临界值
        max_num = 2**31 // 10  # 这里如果是java的话，2的31次方就是负数，只需要转成正数，然后减一就好
        tail_num = 2**31 % 10

        for item in s:
            if (item == "-" or item == "+" or item == " ") and is_negative != None:
                break
            if item == " ":
                continue
            if (item == "-" or item == "+") and is_negative == None:
                is_negative = item == "-"
                continue
            if item.isdigit() != True:
                break
            is_negative=(False if is_negative==None else is_negative)
            temp = int(item)
            # # 这里需要处理溢出 如果已经大于前面的位数，或者等于并且与最后一位相等说明溢出了
            if res > max_num or (
                res == max_num and (temp >= (tail_num if is_negative else tail_num - 1))
            ):
                return -(2**31) if is_negative else 2**31 - 1
            res = res * 10 + int(item)

        return -res if is_negative else res


cc = Solution().myAtoi("  +  413")
print(cc)

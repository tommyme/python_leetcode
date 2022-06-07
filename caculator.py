from collections import deque


def read_num(s):
    num = 0
    for i in s:
        num = num * 10 + int(i)
    return num


def calculator_1(s):
    num = 0
    sign = "+"
    stack = deque()
    s = deque(s)
    l = len(s)

    for i in range(l):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if not s[i].isdigit() or i == l-1:   # s[i] is not digit
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(stack.pop() // num)
            num = 0
            sign = s[i]
    return sum(stack)

calculator_1("1+2*3-4/2")
# [1, 2]
# [1, 6]
# [1, 6, -4]
# [1, 6, -4, -2]
calculator_1("-1+2*3-4/2")
# [0]
# [0, -1, 2]
# [0, -1, 6]
# [0, -1, 6, -4]
# [0, -1, 6, -4, -2]
s = deque("1+((3*(4+1)))+(3)   ")
def calculator_2():
    num = 0
    sign = "+"
    stack = deque()
    while s:       # 尽量不用len
        ch = s.popleft()    # deque 对pop(0)有优化
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "(":
            num = calculator_2()
        # elif ch == ")":
        #     return sum(stack)
        # 对`)`的判断不能放在这里, 因为`)`可能是一个数字的结束, 若在这里判断, 这个数字就没有进入栈中

        if not (ch.isdigit() or ch.isspace()) or not s:   # 尽量不用len
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(stack.pop() // num)
            num = 0
            sign = ch
        if ch == ")":
            return sum(stack)

    return sum(stack)

res = calculator_2()
print(res)

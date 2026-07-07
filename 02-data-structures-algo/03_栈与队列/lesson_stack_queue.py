# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

"""
============================================================
📚 第3课：栈（Stack）与队列（Queue）—— 最简单的线性结构
============================================================
学习目标：
  1. 理解栈的「后进先出」LIFO
  2. 理解队列的「先进先出」FIFO
  3. 掌握 Python 中用 list 和 deque 实现栈/队列
  4. 能解决 LeetCode 经典题（有效括号）

一句话理解：
  栈 = 一摞盘子，后放的先拿
  队列 = 排队买票，先来的先走
"""

from collections import deque

# ============================================================
# 一、栈（Stack）—— 后进先出 LIFO
# ============================================================
# Last In, First Out
#
#   入栈 push →  [值3]
#               [值2]   ← 最后进的在最上面
#               [值1]
#   出栈 pop  →  值3（先拿走最上面的）

print("=" * 40)
print("一、栈（Stack）")
print("=" * 40)

# Python 直接用 list 就行
stack = []

# push（入栈）— 放盘子
stack.append("A")
stack.append("B")
stack.append("C")
print(f"入栈 A,B,C 后: {stack}")  # ['A', 'B', 'C']

# peek（看一眼栈顶）— 不拿走
print(f"栈顶是谁: {stack[-1]}")   # C

# pop（出栈）— 拿走最上面的
print(f"弹出: {stack.pop()}")     # C
print(f"弹出: {stack.pop()}")     # B
print(f"剩下: {stack}")           # ['A']

# 栈空判断
print(f"栈空了吗? {not stack}")   # False（还剩 A）


# ============================================================
# 二、队列（Queue）—— 先进先出 FIFO
# ============================================================
# First In, First Out
#
#   入队 enqueue →  [A, B, C] → 出队 dequeue → A（先来的先走）

print("\n" + "=" * 40)
print("二、队列（Queue）")
print("=" * 40)

# Python 用 collections.deque（双端队列），不要用 list
# list.pop(0) 是 O(n)，deque.popleft() 才是 O(1)
queue = deque()

# enqueue（入队）— 排到队尾
queue.append("张三")
queue.append("李四")
queue.append("王五")
print(f"入队后: {queue}")          # deque(['张三', '李四', '王五'])

# dequeue（出队）— 队头先走
print(f"出队: {queue.popleft()}")  # 张三
print(f"出队: {queue.popleft()}")  # 李四
print(f"剩下: {queue}")            # deque(['王五'])

# 为什么不用 list 做队列？
# list.pop(0) → O(n)，因为后面元素全要前移
# deque.popleft() → O(1)，双端队列专门优化过


# ============================================================
# 三、栈 vs 队列 对比
# ============================================================
"""
          栈 (Stack)              队列 (Queue)
─────────────────────────────────────────────────
规则      LIFO 后进先出           FIFO 先进先出
插入      append() → O(1)        append() → O(1)
删除      pop() → O(1)           popleft() → O(1)
看顶端    stack[-1]              queue[0]
比喻      一摞盘子                排队买票
Python    list                   collections.deque
"""


# ============================================================
# 四、栈的经典应用：括号匹配
# ============================================================
# 判断 "([]{})" 是否合法
# 思路：碰到左括号就入栈，碰到右括号就看栈顶是否匹配

print("\n" + "=" * 40)
print("三、括号匹配")
print("=" * 40)


def is_valid_brackets(s):
    """判断括号字符串是否合法"""
    stack = []
    # 右括号 → 对应的左括号
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in pairs:            # 碰到右括号
            if not stack or stack.pop() != pairs[ch]:
                return False       # 栈顶不匹配 → 非法
        else:
            stack.append(ch)       # 左括号直接入栈

    return not stack               # 栈空才说明全部匹配


print(f'"()" 合法? {is_valid_brackets("()")}')          # True
print(f'"()[]{{}}" 合法? {is_valid_brackets("()[]{}")}')  # True
print(f'"(]" 合法? {is_valid_brackets("(]")}')          # False
print(f'"([)]" 合法? {is_valid_brackets("([)]")}')      # False
print(f'"{{[()]}}" 合法? {is_valid_brackets("{[()]}")}')  # True


# 图解过程：验证 "([])"
"""
字符   栈          说明
─────────────────────────────
(      [(]         左括号入栈
[      [(, []      左括号入栈
]      [(]         ]匹配栈顶[，弹出[
)      []          )匹配栈顶(，弹出(
结束   栈空 → 合法！
"""


# ============================================================
# 五、LeetCode 实战
# ============================================================

# --- LeetCode 20: 有效的括号 ---
# 就是上面的 is_valid_brackets，直接拿去 LeetCode 提交


# --- LeetCode 232: 用栈实现队列 ---
# 用两个栈模拟一个队列
class MyQueue:
    """
    两个栈：一个负责进（push栈），一个负责出（pop栈）
    要出队时，把 push 栈全倒进 pop 栈，顺序就反过来了
    """
    def __init__(self):
        self.stack_in = []    # 入队栈
        self.stack_out = []   # 出队栈

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        self._dump()          # 先倒过来
        return self.stack_out.pop()

    def peek(self):
        self._dump()
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out

    def _dump(self):
        """把入队栈全部倒进出队栈"""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


print("\n" + "=" * 40)
print("四、用栈实现队列")
print("=" * 40)

mq = MyQueue()
mq.push(1)
mq.push(2)
mq.push(3)
print(f"弹出: {mq.pop()}")   # 1
print(f"看一眼: {mq.peek()}")  # 2
print(f"弹出: {mq.pop()}")   # 2
print(f"空了吗? {mq.empty()}")  # False
print(f"弹出: {mq.pop()}")   # 3
print(f"空了吗? {mq.empty()}")  # True


# ============================================================
# 六、时间复杂度总结
# ============================================================
"""
           栈         队列(list)    队列(deque)
──────────────────────────────────────────────
入          O(1)       O(1)         O(1)
出          O(1)       O(n) ❌       O(1) ✅
看顶        O(1)       O(1)         O(1)

关键：用队列一定用 deque，别用 list！
"""


# ============================================================
# 七、练习题
# ============================================================

def practice_valid_parentheses(s):
    """
    【练习题1】有效的括号（LeetCode 20）
    输入: "()[]{}"  → True
    输入: "(]"      → False
    """
    # TODO: 你的代码
    pass


def practice_min_stack():
    """
    【练习题2】最小栈（LeetCode 155 简化版）
    实现一个栈，支持 push、pop、top、getMin，全部 O(1)

    提示：用两个栈，一个存数据，一个存「当前最小值」
    """
    # TODO: 你的代码
    pass


# ============================================================
# 八、常见坑
# ============================================================
"""
坑1: 用 list 做队列
  ❌ queue.pop(0)    # O(n)，数据量大时巨慢
  ✅ deque.popleft() # O(1)

坑2: 栈空时取栈顶
  ❌ stack[-1]       # 空列表 → IndexError
  ✅ if stack: x = stack[-1]

坑3: 括号匹配不检查剩余
  ❌ 只检查栈顶忽略最后栈不为空 → "(((" 会判合法
  ✅ return not stack（最后必须空）

坑4: deque 要先 import
  ❌ from collections import deque
  别忘了这行
"""

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ 第3课「栈与队列」学习完成！")
    print("核心：栈=LIFO（一摞盘子），队列=FIFO（排队买票）")
    print("下一步：手写括号匹配 → LeetCode 20 / 232 / 155")
    print("=" * 60)

    # 练习题测试
    print("\n📝 练习题测试：")
    result = practice_valid_parentheses("()[]{}")
    if result is True:
        print("  ✅ 练习题1 有效括号: True (输入 '()[]{}')")
    elif result is False:
        print("  ❌ 练习题1 预期 True，实际 False")
    else:
        print("  ⚠️  练习题1 还没写")

    result = practice_valid_parentheses("(]")
    if result is False:
        print("  ✅ 练习题1 有效括号: False (输入 '(]')")
    elif result is True:
        print("  ❌ 练习题1 预期 False，实际 True")

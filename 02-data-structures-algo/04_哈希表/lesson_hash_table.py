# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

"""
============================================================
📚 第4课：哈希表（Hash Table）—— 你已经用了三遍的东西
============================================================
学习目标：
  1. 理解哈希表的核心思想：key → 数组下标
  2. 掌握 Python dict 的常用操作
  3. 能解决计数、去重、映射类 LeetCode 题

一句话理解：
  哈希表 = 带编号的储物柜。给你一个 key，瞬间算出柜子编号，直接开柜门。
"""

# ============================================================
# 一、你已经用过的哈希表
# ============================================================
"""
回顾前面你写的代码：

# 两数之和
seen = {}           # {数值: 索引}
seen[num] = i

# 环形链表判重
slow == fast

# 括号匹配
pairs = {')': '(', ']': '[', '}': '{'}

这些都是哈希表！Python 的 dict 和 set 底层就是哈希表。
"""

# ============================================================
# 二、哈希表是怎么做到的？
# ============================================================
"""
例子：存「姓名 → 学号」

没有哈希表的话，要查 '张三' 的学号，得翻完整张表（O(n)）。

哈希表的做法：
  '张三' → 哈希函数 → 数组[7] → 学号就在这里

key → hash(key) → 数组下标 → O(1)

不管表里存了 100 条还是 100 万条数据，查 key 都是 O(1)。
"""

# ============================================================
# 三、Python 中的哈希表：dict 和 set
# ============================================================

# dict：存 key → value
print("=" * 40)
print("一、dict 基本操作")
print("=" * 40)

d = {}
d['apple'] = 3        # 插入
d['banana'] = 5
print(f"apple 数量: {d['apple']}")  # 取值
print(f"banana 在吗? {'banana' in d}")  # 判断存在 O(1)

# 遍历
for key, val in d.items():
    print(f"  {key}: {val}")

# set：只存 key，不存 value（去重用）
print("\n" + "=" * 40)
print("二、set 基本操作")
print("=" * 40)

s = {1, 2, 3}
s.add(4)              # 插入
s.add(2)              # 重复的加不进去
print(f"set: {s}")    # {1, 2, 3, 4}
print(f"3 在吗? {3 in s}")  # O(1) 判断


# ============================================================
# 四、哈希表的三种经典用法
# ============================================================

# 用法1：计数（统计频率）
print("\n" + "=" * 40)
print("三、计数字符出现次数")
print("=" * 40)

def count_chars(s):
    """统计每个字符出现多少次"""
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    return count

# count.get(ch, 0)：有就返回，没有就返回 0
print(f"'hello' 计数: {count_chars('hello')}")
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# 用法2：去重（看看有没有出现过）
print("\n" + "=" * 40)
print("四、去重判断")
print("=" * 40)

def has_duplicate(nums):
    """判断数组有没有重复元素"""
    seen = set()
    for num in nums:
        if num in seen:
            return True       # 见过了！
        seen.add(num)
    return False

print(f"[1,2,3,1] 有重复? {has_duplicate([1, 2, 3, 1])}")  # True
print(f"[1,2,3] 有重复? {has_duplicate([1, 2, 3])}")     # False


# 用法3：映射（找对应关系）
print("\n" + "=" * 40)
print("五、映射查找")
print("=" * 40)

def two_sum_map(nums, target):
    """两数之和 — 你写过的"""
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

print(f"两数之和 target=9: {two_sum_map([2, 7, 11, 15], 9)}")


# ============================================================
# 五、时间复杂度
# ============================================================
"""
dict / set 的操作：
  插入  O(1) 平均
  删除  O(1) 平均
  查找  O(1) 平均

都是 O(1)！前提是 hash 函数均匀分布。

vs 数组查找 O(n)：
  数组 100 万个元素，最坏要翻 100 万次
  哈希表查 key，1 次到位
"""


# ============================================================
# 六、练习题
# ============================================================

def practice_contains_duplicate(nums):
    """
    【练习题1】存在重复元素（LeetCode 217）
    输入: [1,2,3,1] → True
    输入: [1,2,3] → False
    提示：用 set 记录见过的元素
    """
    # TODO: 你的代码
    seen = set()
    for num in nums:
        if num in seen:
            return True      # 找到了重复！
        seen.add(num)
    return False             # 走完没找到


def practice_is_anagram(s, t):
    """
    【练习题2】有效的字母异位词（LeetCode 242）
    输入: s="anagram", t="nagaram" → True（字母相同，排列不同）
    输入: s="rat", t="car" → False
    提示：统计两个字符串每个字符的出现次数，比较是否相同
    """
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}
    for ch in s:
        count_s[ch] = count_s.get(ch, 0) + 1
    for ch in t:
        count_t[ch] = count_t.get(ch, 0) + 1

    return count_s == count_t


# ============================================================
# 七、技巧速记
# ============================================================
"""
❶ dict 找搭档      seen = {}; if target-x in seen
❷ set 判重         seen = set(); if x in seen
❸ 计数             d[x] = d.get(x, 0) + 1
❹ 字符串映射       pairs = {...}
❺ 两数组交集       用 set 的 & 运算符
"""


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ 第4课「哈希表」学习完成！")
    print("核心：key → hash → 数组下标 → O(1)")
    print("dict 查 key、set 判重、计数统计 — 三板斧")
    print("下一步：练习题2道 → LeetCode 217 / 242 / 349")
    print("=" * 60)

    # 练习题测试
    print("\n📝 练习题测试：")
    result = practice_contains_duplicate([1, 2, 3, 1])
    if result is True:
        print("  ✅ 练习题1 存在重复: True")
    elif result is False:
        print("  ❌ 练习题1 预期 True，实际 False")
    else:
        print("  ⚠️  练习题1 还没写")

    result = practice_is_anagram("anagram", "nagaram")
    if result is True:
        print("  ✅ 练习题2 字母异位词: True")
    elif result is False:
        print("  ❌ 练习题2 预期 True，实际 False")
    else:
        print("  ⚠️  练习题2 还没写")

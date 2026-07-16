# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

"""
============================================================
📚 第9课：搜索算法 —— 怎么找到目标
============================================================
学习目标：
  1. 掌握二分查找（有序数组 O(log n) 搜索）
  2. 回顾 BFS/DFS 的搜索本质
  3. 理解「搜索」=「在解空间中找目标」

一句话理解：
  搜索 = 找东西。线性搜索 = 一个个翻（O(n)）；二分搜索 = 砍一半（O(log n)）。
  BFS/DFS = 在图/树的解空间里搜索。
"""

# ============================================================
# 一、线性搜索 — 你早就写过的
# ============================================================
"""
从头到尾一个个找，O(n)。最朴素的方式。
"""
print("=" * 50)
print("一、线性搜索 vs 二分搜索")
print("=" * 50)


def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [1, 5, 8, 12, 20]
print(f"线性搜索 8 在索引: {linear_search(arr, 8)}")  # 2


# ============================================================
# 二、二分搜索 — 砍一半（核心！）
# ============================================================
"""
前提：数组必须有序

[1, 5, 8, 12, 20]  找 12
 L=0    M=2    R=4
        ↑ 8<12 → 右边搜 [12,20]
 砍左边！

每次砍一半 → O(log n)。100万个元素只需 20 步。
"""


def binary_search(arr, target):
    """二分查找，返回索引，没找到返回 -1"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid           # 找到了
        elif arr[mid] < target:
            left = mid + 1       # 目标在右边
        else:
            right = mid - 1      # 目标在左边
    return -1                    # 没找到


print(f"二分搜索 12 在索引: {binary_search(arr, 12)}")  # 3
print(f"二分搜索 7 在索引: {binary_search(arr, 7)}")    # -1

# 图解：[1, 5, 8, 12, 20] 找 12
"""
第1轮: left=0, right=4, mid=2, arr[2]=8 < 12 → left=3
第2轮: left=3, right=4, mid=3, arr[3]=12 找到了！返回 3
"""


# ============================================================
# 三、二分搜索的两个变体（面试常考）
# ============================================================

# 变体1：找左边界（第一个 >= target 的位置）
def lower_bound(arr, target):
    """
    找到第一个 >= target 的索引
    [1, 3, 3, 5, 7] target=3 → 返回 1（第一个3的位置）
    """
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid        # arr[mid] >= target，可能是答案
    return left


arr2 = [1, 3, 3, 5, 7]
print(f"\n变体测试: {arr2}")
print(f"  第一个 >= 3 的位置: {lower_bound(arr2, 3)}")   # 1
print(f"  第一个 >= 4 的位置: {lower_bound(arr2, 4)}")   # 3（5的位置）


# ============================================================
# 四、搜索的本质 = 在解空间找目标
# ============================================================
"""
二分搜索：在「有序数组」里找目标值
BFS：      在「图/树的层」里找目标节点
DFS：      在「图/树的分支」里找目标节点
回溯：     在「所有可能组合」里找目标解    ← 下章学

搜索 = 定义解空间 + 选择搜索策略（线性的/二分的/广度的/深度的）
"""

# ============================================================
# 五、BFS/DFS 回顾 —— 图搜索
# ============================================================
print("\n" + "=" * 50)
print("二、BFS/DFS 搜索回顾")
print("=" * 50)

"""
你已经在图那章学过了：

二分搜索  → 有序数组 → 每次砍一半
BFS       → 图/网格   → 一层层扩散（用队列）
DFS       → 图/网格   → 一条路走到底（用递归）

本质都是「搜索」：在数据结构中找目标。
"""


# ============================================================
# 六、容易混淆的模板
# ============================================================
"""
二分查找模板（背下来）：

  left, right = 0, len(arr) - 1
  while left <= right:
      mid = (left + right) // 2
      if arr[mid] == target:
          return mid           # 找到了
      elif arr[mid] < target:
          left = mid + 1       # 目标在右边，砍左
      else:
          right = mid - 1      # 目标在左边，砍右
  return -1                    # 没找到

核心：<= 不是 <，mid+1/mid-1 不是 mid。
"""

# ============================================================
# 七、练习题
# ============================================================

def practice_binary_search(arr, target):
    """
    【练习题1】手写二分查找
    输入: arr=[1,5,8,12,20], target=12 → 输出: 3
    输入: arr=[1,5,8,12,20], target=7 → 输出: -1
    """
    # TODO: 你的代码
    pass


def practice_search_insert(nums, target):
    """
    【练习题2】搜索插入位置（LeetCode 35）
    输入: nums=[1,3,5,6], target=5 → 输出: 2
    输入: nums=[1,3,5,6], target=2 → 输出: 1（应该插在索引1）
    输入: nums=[1,3,5,6], target=7 → 输出: 4（应该插在末尾）
    提示：就是 lower_bound
    """
    # TODO: 你的代码
    pass


# ============================================================
# 八、常见坑
# ============================================================
"""
坑1: while left <= right
  ❌ while left < right   → 只剩一个元素时跳过了
  ✅ while left <= right

坑2: mid 更新
  ❌ left = mid   → 死循环
  ✅ left = mid + 1  或  right = mid - 1

坑3: 忘了数组必须有序
  ❌ [3,1,5,2] 跑二分
  ✅ 二分只能用于有序数组

坑4: 整数溢出（Python 没这问题）
  ❌ mid = (left + right) // 2  其他语言会溢出
  ✅ Python 大整数安全
"""

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ 第9课「搜索算法」学习完成！")
    print("核心：二分搜索 O(log n) — 有序数组神器")
    print("下一步：手写二分查找 → LeetCode 704 / 35")
    print("=" * 60)

    print("\n📝 练习题测试：")
    result = practice_binary_search([1, 5, 8, 12, 20], 12)
    if result == 3:
        print("  ✅ 练习题1 二分查找: 索引3")
    elif result is None:
        print("  ⚠️  练习题1 还没写")
    else:
        print(f"  ❌ 练习题1 预期 3，实际 {result}")

    result = practice_binary_search([1, 5, 8, 12, 20], 7)
    if result == -1:
        print("  ✅ 练习题1 二分查找: -1（没找到）")
    elif result is None:
        pass
    else:
        print(f"  ❌ 练习题1 预期 -1，实际 {result}")

    result = practice_search_insert([1, 3, 5, 6], 2)
    if result == 1:
        print("  ✅ 练习题2 插入位置: 1")
    elif result is None:
        print("  ⚠️  练习题2 还没写")
    else:
        print(f"  ❌ 练习题2 预期 1，实际 {result}")

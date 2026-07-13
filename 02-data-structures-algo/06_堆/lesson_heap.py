# -*- coding: utf-8 -*-
import sys
import heapq
sys.stdout.reconfigure(encoding='utf-8')

"""
============================================================
📚 第6课：堆（Heap）—— 自动排好队的最小值
============================================================
学习目标：
  1. 理解堆的结构：完全二叉树 + 堆性质
  2. 掌握 Python heapq 的 push / pop / peek
  3. 能解决 Top K 类问题

一句话理解：
  堆 = 一个会自动把最小值推到最上面的数据结构。
  每次 push 或 pop 后，最小值永远在堆顶。O(log n) 插入，O(1) 看堆顶。
"""

# ============================================================
# 一、堆是什么？
# ============================================================
"""
堆是「完全二叉树」+「堆性质」：

        1              ← 堆顶（最小值）
       / \
      3   2            ← 每个父节点 <= 子节点
     / \ / \
    7  4 5  6

规则（最小堆）：每个父节点 <= 所有子节点
结果：最上面那个永远是全堆最小的！

最大堆反过来：每个父节点 >= 子节点，堆顶最大值。

Python 的 heapq 是最小堆。
"""

# ============================================================
# 二、Python heapq 操作
# ============================================================
print("=" * 50)
print("一、堆的基本操作")
print("=" * 50)

# 准备一堆乱数
nums = [5, 2, 9, 1, 7, 3]

# 1. 建堆：把列表变成堆
heap = nums[:]          # 复制一份，不污染原列表
heapq.heapify(heap)
print(f"建堆后: {heap}")  # [1, 2, 3, 5, 7, 9]
print(f"堆顶(最小): {heap[0]}")  # 1，O(1)

# 2. push：插入一个数
heapq.heappush(heap, 4)
print(f"push 4 后: {heap}")  # [1, 2, 3, 5, 7, 9, 4]

# 3. pop：弹出最小值
min_val = heapq.heappop(heap)
print(f"弹出最小值: {min_val}")  # 1
print(f"现在堆: {heap}")         # [2, 4, 3, 5, 7, 9]

# 4. 再弹
print(f"再弹: {heapq.heappop(heap)}")  # 2
print(f"再弹: {heapq.heappop(heap)}")  # 3

# 5. push + pop 合体：插入一个并弹出最小值（效率更高）
heapq.heappush(heap, 1)     # 先推一个
print(f"\n当前堆: {heap}")
result = heapq.heappushpop(heap, 6)
print(f"push 6 后弹出最小: {result}")  # 1


# ============================================================
# 三、为什么堆这么快？
# ============================================================
"""
对比：

            push         pop          peek(看最小)
────────────────────────────────────────────────
数组(未排序)   O(1)        O(n) 遍历找     O(n)
数组(排序)    O(n) 插入    O(1)            O(1)
堆            O(log n)    O(log n)        O(1) ✅

堆的 log n 来自完全二叉树的高度：100万个数只有 20 层。
push/pop 只需要上下调整 20 步，非常快。
"""


# ============================================================
# 四、堆的经典应用：Top K 问题
# ============================================================
print("\n" + "=" * 50)
print("二、Top K 问题")
print("=" * 50)

# 问题：找数组中第 K 大的元素
# 思路：维护一个大小为 K 的最小堆
#      - 堆里的元素是「当前见到的最大的 K 个」
#      - 堆顶是这 K 个中最小的那个 → 即第 K 大的元素

def find_kth_largest(nums, k):
    """
    找第 k 大的元素（LeetCode 215）
    思路：大小为 k 的最小堆，堆顶即第 k 大
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:           # 堆超过 k 了
            heapq.heappop(heap)     # 把最小的踢出去
    return heap[0]                   # 堆顶 = 第 k 大


nums = [3, 2, 1, 5, 6, 4]
print(f"数组: {nums}")
print(f"第 1 大: {find_kth_largest(nums, 1)}")  # 6
print(f"第 2 大: {find_kth_largest(nums, 2)}")  # 5
print(f"第 3 大: {find_kth_largest(nums, 3)}")  # 4


# 推演：找第 2 大的元素
"""
nums = [3, 2, 1, 5, 6, 4], k=2

num=3: push 3 → heap=[3]
num=2: push 2 → heap=[2,3]
num=1: push 1 → heap=[1,3,2]  → 超了，pop 1 → heap=[2,3]
num=5: push 5 → heap=[2,3,5]  → 超了，pop 2 → heap=[3,5]
num=6: push 6 → heap=[3,5,6]  → 超了，pop 3 → heap=[5,6]
num=4: push 4 → heap=[4,6,5]  → 超了，pop 4 → heap=[5,6]

堆里始终保留「最大的 2 个」→ 堆顶 5 是第 2 大
"""


# ============================================================
# 五、最大堆的技巧
# ============================================================
# Python 只有最小堆。怎么实现最大堆？取负数！

nums = [5, 2, 9, 1, 7]
max_heap = [-x for x in nums]   # 全取负
heapq.heapify(max_heap)
print(f"\n最大堆（负数版）: {max_heap}")  # [-9, -7, -5, -1, -2]
print(f"最大值: {-max_heap[0]}")          # 9
heapq.heappush(max_heap, -10)            # push 10（存 -10）
print(f"push 10 后最大值: {-heapq.heappop(max_heap)}")  # 10


# ============================================================
# 六、练习题
# ============================================================

def practice_kth_largest(nums, k):
    """
    【练习题1】数组中的第K个最大元素（LeetCode 215）
    输入: nums=[3,2,1,5,6,4], k=2 → 输出: 5
    提示：维护大小为 k 的最小堆
    """
    # TODO: 你的代码
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


def practice_kth_smallest(nums, k):
    """
    【练习题2】第 K 个最小元素
    输入: nums=[3,2,1,5,6,4], k=2 → 输出: 2
    提示：用最大堆（取负数），维护大小为 k
    """
    # TODO: 你的代码
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
        if len(heap) > k:
            heapq.heappop(heap)
    return -heap[0]

# ============================================================
# 七、常见坑
# ============================================================
"""
坑1: 忘了 import
  ❌ heapq.heappush(...)
  ✅ from heapq import ...  or  import heapq

坑2: 堆顶读取
  ❌ heap.pop()  → list 的 pop，不是堆操作！
  ✅ heap[0]  → O(1) 查看最小值

坑3: 最大堆
  ❌ Python 没有 max-heap
  ✅ 所有数取负数，或 heapq 存的都是 (priority, item) 元组

坑4: 堆不是完全排序的
  ❌ print(heap) 可能看到 [1, 5, 3, 7, 9] → 以为没排序
  ✅ 堆不保证全序，只保证 heap[0] 是最小的
"""

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ 第6课「堆」学习完成！")
    print("核心：O(log n) 插入/删除，O(1) 取最小，Top K 神器")
    print("下一步：手写 Top K → LeetCode 215")
    print("=" * 60)

    # 练习题测试
    print("\n📝 练习题测试：")
    result = practice_kth_largest([3, 2, 1, 5, 6, 4], 2)
    if result == 5:
        print("  ✅ 练习题1 第K大: 5")
    elif result is None:
        print("  ⚠️  练习题1 还没写")
    else:
        print(f"  ❌ 练习题1 预期 5，实际 {result}")

    result = practice_kth_smallest([3, 2, 1, 5, 6, 4], 2)
    if result == 2:
        print("  ✅ 练习题2 第K小: 2")
    elif result is None:
        print("  ⚠️  练习题2 还没写")
    else:
        print(f"  ❌ 练习题2 预期 2，实际 {result}")

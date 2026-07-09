# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

"""
============================================================
📚 第1课：数组（Array）—— 算法世界的基石
============================================================
学习目标：
  1. 理解数组的「连续内存」存储特点
  2. 掌握数组的 CRUD 操作（增删改查）及时间复杂度
  3. 能用数组解决 LeetCode 入门题

一句话理解：
  数组 = 一排连续编号的储物柜，每个柜子存一个数据，按编号直接访问。
"""

# ============================================================
# 一、数组的三个核心特性
# ============================================================

# 【特性1：连续存储】
# 数组在内存中是一块连续的地址空间，像一排紧挨着的停车位。
# 好处：知道第一个位置 + 偏移量，就能瞬间算出任意位置 → O(1) 访问

# 【特性2：索引访问 O(1)】
# 数组最大的优势——按下标查找是「瞬间」的
arr = [10, 20, 30, 40, 50]
print(f"arr[0] = {arr[0]}")   # 第一个元素 → 10
print(f"arr[3] = {arr[3]}")   # 第四个元素 → 40
print(f"arr[-1] = {arr[-1]}") # 最后一个元素 → 50（Python独有语法糖）

# 【特性3：插入/删除很慢 O(n)】
# 因为要挪位置——想象一排书中间要插入一本，后面的书都得往后移


# ============================================================
# 二、数组的基本操作（自己实现，理解原理）
# ============================================================

# --- 1. 尾部插入 O(1) ---
# 末尾有空位，直接放进去就行
arr = [1, 2, 3]
arr.append(4)          # Python内置，O(1)
print(f"尾部插入后: {arr}")  # [1, 2, 3, 4]

# --- 2. 中间插入 O(n) ---
# 位置2插入99，后面的元素都得往后移
arr = [1, 2, 3, 4, 5]
arr.insert(2, 99)      # 在索引2插入99
print(f"中间插入后: {arr}")  # [1, 2, 99, 3, 4, 5]

# --- 3. 查找元素 O(n) ---
# 最坏情况：要找的在最后，得遍历整个数组
arr = [10, 20, 30, 40, 50]
target = 30
for i in range(len(arr)):
    if arr[i] == target:
        print(f"找到了！索引在 {i}")
        break

# --- 4. 删除元素 O(n) ---
# 删除中间的元素，后面的补上来
arr = [1, 2, 99, 3, 4]
arr.remove(99)         # 按值删除，O(n)
print(f"删除后: {arr}")  # [1, 2, 3, 4]

del arr[1]             # 按索引删除，O(n)
print(f"按索引删除后: {arr}")  # [1, 3, 4]

# --- 5. 遍历数组 O(n) ---
arr = [10, 20, 30, 40, 50]
# 方法1：按索引遍历（当你需要知道索引时用）
for i in range(len(arr)):
    print(f"arr[{i}] = {arr[i]}", end=" | ")
print()

# 方法2：直接遍历元素（最常用）
for num in arr:
    print(num, end=" ")
print()


# ============================================================
# 三、时间复杂度速查表（面试必知）
# ============================================================
"""
操作          时间复杂度     为什么
──────────────────────────────────────────
按索引访问     O(1)       地址连续，直接计算
尾部插入       O(1)       末尾有空位
中间插入       O(n)       要挪动后面的元素
按值查找       O(n)       要一个一个找
按索引删除     O(n)       后面元素要前移
遍历           O(n)       每个看一遍
"""


# ============================================================
# 四、常考技巧：双指针（Two Pointers）
# ============================================================
# 双指针是数组题目最常用的技巧
# 核心思想：两个指针从不同位置出发，根据条件向中间（或同向）移动

# 例题：反转数组（原地反转，不用额外空间）
def reverse_array(arr):
    """用双指针反转数组，不需要额外数组"""
    left, right = 0, len(arr) - 1
    while left < right:
        # 交换左右两端的元素
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

print(f"反转[1,2,3,4,5] → {reverse_array([1, 2, 3, 4, 5])}")


# ============================================================
# 五、LeetCode 入门实战
# ============================================================

# --- LeetCode 1: 两数之和 (Two Sum) ---
# 给定一个整数数组 nums 和一个目标值 target，
# 请找出数组中和为目标值的两个数的索引。
# 你可以假设每种输入只会对应一个答案，且不能重复使用同一个元素。

def two_sum(nums, target):
    """
    思路：用哈希表记录「已经遍历过的数」
    遍历到 x 时，查 target - x 是否在哈希表里
    时间复杂度 O(n)，空间复杂度 O(n)
    """
    seen = {}  # {数值: 索引}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # 没找到

print(f"两数之和 [2,7,11,15] target=9 → {two_sum([2, 7, 11, 15], 9)}")  # [0, 1]


# --- LeetCode 26: 删除有序数组中的重复项 ---
# 原地删除重复项，返回新长度

def remove_duplicates(nums):
    """
    思路：快慢指针
    slow 指向「已去重部分」的末尾
    fast 在前方探路，遇到新元素就放到 slow+1
    """
    if not nums:
        return 0
    slow = 0  # 已去重部分的最后索引
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1  # 新长度

nums = [1, 1, 2, 2, 3, 4, 4]
new_len = remove_duplicates(nums)
print(f"去重后长度={new_len}, 数组={nums[:new_len]}")  # 长度=4, [1,2,3,4]


# --- LeetCode 283: 移动零 ---
# 把所有0移到数组末尾，保持非零元素的相对顺序

def move_zeroes(nums):
    """
    思路：快慢指针，慢指针指向「下一个非零应该放的位置」
    """
    slow = 0  # 下一个非零元素应该放的位置
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

print(f"移动零 [0,1,0,3,12] → {move_zeroes([0, 1, 0, 3, 12])}")  # [1,3,12,0,0]


# ============================================================
# 六、练习题（自己动手，巩固理解）
# ============================================================
# 以下题目建议你先不看答案，自己动手实现

def practice_merge_sorted_arrays(arr1, arr2):
    """
    【练习题1】合并两个有序数组（LeetCode 88 简化版）
    输入: arr1=[1,3,5], arr2=[2,4,6]
    输出: [1,2,3,4,5,6]
    提示：用两个指针分别指向两个数组
    """
    # 双指针合并：两个手指分别指两个数组，每次取小的
    result = []
    i, j = 0, 0  # i 指向 arr1，j 指向 arr2

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # 把剩下没比完的直接追加（其中一个已经空了）
    result.extend(arr1[i:])  # arr1 剩下的
    result.extend(arr2[j:])  # arr2 剩下的
    return result


def practice_max_subarray(nums):
    """
    【练习题2】最大子数组和（LeetCode 53 简化版）
    输入: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    输出: 6  （子数组 [4,-1,2,1] 的和最大）
    提示：动态规划思想，但可以先尝试暴力遍历
    """
    # TODO: 你的代码写在这里
    max_num = float("-inf")
    for start in range(len(nums)):
        for end in range(start, len(nums)):
            sub = nums[start: end + 1]
            total = sum(sub)
            if total > max_num:
                max_num = total
    return max_num
        


# ============================================================
# 七、常见坑（新手易错）
# ============================================================
"""
坑1: 遍历时修改数组
  ❌ for num in arr: arr.remove(num)   # 会跳过元素！
  ✅ 创建一个新列表，或者从后往前遍历

坑2: 边界条件
  ❌ 忘记检查空数组 → arr[0] 直接报错
  ✅ 先写 if not arr: return

坑3: 数组越界
  ❌ for i in range(len(arr)+1): arr[i]  # 最后会越界
  ✅ for i in range(len(arr)): arr[i]

坑4: 浅拷贝陷阱
  ❌ arr2 = arr1; arr2[0]=999  # 改了arr2, arr1也变了！
  ✅ arr2 = arr1[:] 或 arr2 = arr1.copy()
"""

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ 第1课「数组」学习完成！")
    print("下一步：完成两道练习题 → 去LeetCode刷Easy题 → 进入链表")
    print("=" * 60)

    print("\n📝 练习题测试：")

    # 测试合并有序数组
    result = practice_merge_sorted_arrays([1, 3, 5], [2, 4, 6])
    if result == [1, 2, 3, 4, 5, 6]:
        print(f"  ✅ 练习题1 合并有序数组: {result}")
    elif result is None:
        print("  ⚠️  练习题1 还没写（pass了）")
    else:
        print(f"  ❌ 练习题1 预期 [1,2,3,4,5,6]，实际 {result}")

    # 测试最大子数组和
    result = practice_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    if result == 6:
        print(f"  ✅ 练习题2 最大子数组和: {result}")
    elif result is None:
        print("  ⚠️  练习题2 还没写（pass了）")
    else:
        print(f"  ❌ 练习题2 预期 6，实际 {result}")

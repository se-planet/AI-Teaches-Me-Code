# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

"""
============================================================
📚 第2课：链表（Linked List）—— 数组的互补兄弟
============================================================
学习目标：
  1. 理解链表的「节点 + 指针」存储方式
  2. 对比链表和数组的优缺点
  3. 手写链表的遍历、插入、删除
  4. 能用链表解决 LeetCode 入门题

一句话理解：
  链表 = 火车，每节车厢（节点）上写着数据，车厢之间用钩子（指针）连起来。
  要访问第10节车厢？必须从第1节开始，一节一节走过去。
"""


# ============================================================
# 一、链表 vs 数组 —— 一张表看清楚
# ============================================================
"""
                数组                          链表
──────────────────────────────────────────────────────
内存存储    |  连续的一块                    随便散落，靠指针连着
索引访问    |  O(1) 瞬间定位                 O(n) 必须从头走
插入/删除   |  O(n) 要挪位置                 O(1) 改指针就行
查找        |  O(n)                          O(n)
比喻        |  一排紧挨的停车位              一列靠铁链连着的火车
"""


# ============================================================
# 二、定义链表节点
# ============================================================

class ListNode:
    """链表节点：一个数据槽 + 一个指向下一个节点的指针"""
    def __init__(self, val=0, next=None):
        self.val = val      # 节点存的数据
        self.next = next    # 指向下一个节点（没指向就是None，末尾）

    def __repr__(self):
        return f"ListNode({self.val})"


# 手动造一个链表：1 → 2 → 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
# 现在 node1 就是整个链表的头：1 → 2 → 3

print("手动创建链表：", end="")
cur = node1
while cur:
    print(cur.val, end=" → " if cur.next else "\n")
    cur = cur.next


# ============================================================
# 三、链表的基本操作
# ============================================================

# --- 1. 遍历链表 O(n) ---
def traverse(head):
    """从头走到尾，打印每个节点"""
    cur = head
    result = []
    while cur:              # cur 是 None 说明到末尾了
        result.append(cur.val)
        cur = cur.next      # 走到下一节车厢
    return result

# 造链表的小工具：数组 → 链表
def make_list(arr):
    """把数组转成链表，方便测试"""
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

head = make_list([10, 20, 30, 40, 50])
print(f"遍历结果: {traverse(head)}")  # [10, 20, 30, 40, 50]


# --- 2. 在头部插入 O(1) ---
def insert_at_head(head, val):
    """在链表头部插入新节点，返回新的头"""
    new_node = ListNode(val)
    new_node.next = head     # 新节点指向旧的头
    return new_node          # 新节点成为新的头

head = make_list([2, 3, 4])
head = insert_at_head(head, 1)
print(f"头部插入后: {traverse(head)}")  # [1, 2, 3, 4]


# --- 3. 在尾部插入 O(n) ---
def insert_at_tail(head, val):
    """走到末尾，挂上新节点"""
    new_node = ListNode(val)
    if not head:
        return new_node
    cur = head
    while cur.next:          # 走到最后一节
        cur = cur.next
    cur.next = new_node      # 挂上新车厢
    return head

head = make_list([1, 2, 3])
head = insert_at_tail(head, 4)
print(f"尾部插入后: {traverse(head)}")  # [1, 2, 3, 4]


# --- 4. 删除节点 O(n) ---
def delete_by_val(head, val):
    """删除第一个值为 val 的节点"""
    # 特殊情况：删的是头节点
    if head and head.val == val:
        return head.next      # 把头扔掉，返回下一个

    cur = head
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next  # 跳过要删的节点
            break
        cur = cur.next
    return head

head = make_list([1, 99, 2, 3])
head = delete_by_val(head, 99)
print(f"删除 99 后: {traverse(head)}")  # [1, 2, 3]


# ============================================================
# 四、链表的时间复杂度
# ============================================================
"""
操作             复杂度      原因
────────────────────────────────────────
头部插入          O(1)      改一个指针就行
尾部插入          O(n)      要先走到末尾
中间插入          O(n)      要先走到那个位置
删除              O(n)      要先找到要删的
查找              O(n)      必须从头遍历
索引访问          O(n)      不能像数组一样直接跳
"""


# ============================================================
# 五、关键技巧 —— 反复出现的手写题
# ============================================================

# --- 1. 反转链表（LeetCode 206，链表必刷题）---
def reverse_list(head):
    """
    思路：逐个把箭头方向反过来
    1 → 2 → 3 → None  变成  None ← 1 ← 2 ← 3

    用 prev, cur, nxt 三个指针协作
    核心：cur.next = prev（把当前箭头反过来指）
    """
    prev = None           # 前一个节点（最终会成为新的尾）
    cur = head            # 当前处理的节点
    while cur:
        nxt = cur.next    # 先把后面的记下来（不然断了找不到了）
        cur.next = prev   # 反转箭头：当前指向前一个
        prev = cur        # prev 前进一步
        cur = nxt         # cur 前进一步
    return prev           # prev 成为了新的头

def reverse_list2(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


head = make_list([1, 2, 3, 4, 5])
reversed_head = reverse_list(head)
print(f"反转后: {traverse(reversed_head)}")  # [5, 4, 3, 2, 1]


# --- 2. 找链表中点（快慢指针经典应用）---
def find_middle(head):
    """
    快指针每次走两步，慢指针每次走一步
    快指针到终点时，慢指针刚好在中间
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next       # 慢的一步
        fast = fast.next.next  # 快的两步
    return slow.val if slow else None

def find_middle2(head):
    slow = fast = head
    while fast and fast.next:
        slow = head.next
        fast = head.next.next
    return slow.val if slow else None

head = make_list([1, 2, 3, 4, 5])
print(f"链表中点: {find_middle(head)}")  # 3

head = make_list([1, 2, 3, 4])
print(f"链表中点(偶数): {find_middle(head)}")  # 3（偏右）


# --- 3. 合并两个有序链表（LeetCode 21）---
def merge_two_lists(l1, l2):
    """
    和合并有序数组一样，双指针比大小。
    区别：数组用索引，链表用 next 指针。
    """
    dummy = ListNode(0)   # 哑节点（哨兵），简化边界处理
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next

    cur.next = l1 or l2    # 剩下没比完的直接接上
    return dummy.next      # 返回哑节点后面的真正头节点

def merge_two_list2(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.next < l2.next:
            cur.next = l1
            l1 = l1.next
        else:
            l2.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

l1 = make_list([1, 3, 5])
l2 = make_list([2, 4, 6])
merged = merge_two_lists(l1, l2)
print(f"合并有序链表: {traverse(merged)}")  # [1, 2, 3, 4, 5, 6]


# ============================================================
# 六、LeetCode 入门实战
# ============================================================

# --- LeetCode 141: 环形链表 ---
def has_cycle(head):
    """
    判断链表有没有环（尾巴指向了前面的某个节点）

    思路：快慢指针
    - 有环 → 快慢指针最终会相遇（在操场上跑圈，快的迟早追上慢的）
    - 无环 → 快指针会走到末尾 None
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 造一个带环的链表：1 → 2 → 3 → 4 → 2（回到2）
n1, n2, n3, n4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2  # n4 指向 n2，形成环
print(f"有环? {has_cycle(n1)}")  # True

head = make_list([1, 2, 3, 4])
print(f"无环链表有环? {has_cycle(head)}")  # False


# ============================================================
# 七、练习题
# ============================================================

def practice_reverse_list(head):
    """
    【练习题1】反转链表 —— 不看上面的代码，自己手写一遍

    输入: 1 → 2 → 3 → 4 → 5
    输出: 5 → 4 → 3 → 2 → 1

    提示：三个指针 prev, cur, nxt
    """
    # TODO: 你的代码
    prev = None
    cur = head
    while cur:
        nxt = cur.next      # ① 先记后路！
        cur.next = prev     # ② 箭头调头
        prev = cur          # ③ prev 前移
        cur = nxt           # ④ cur 前移
    return prev             # 别忘了返回新的头


def practice_remove_nth_from_end(head, n):
    """
    【练习题2】删除链表的倒数第 N 个节点（LeetCode 19 简化版）

    输入: 1 → 2 → 3 → 4 → 5, n=2
    输出: 1 → 2 → 3 → 5   （删掉倒数第2个，即4）

    提示：快指针先走 n 步，然后快慢一起走，慢的就停在了要删的位置前
    """
    # TODO: 你的代码
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    # 特殊情况：要删的是头节点（n == 链表长度）
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head



# ============================================================
# 八、链表常见坑
# ============================================================
"""
坑1: 操作空链表
  ❌ head.next  →  head 是 None 就报错
  ✅ 先判断 if not head: return

坑2: 修改指针后找不到后面的节点
  ❌ cur.next = xxx   # 没保存原来的 cur.next，后面丢了
  ✅ nxt = cur.next; cur.next = xxx; cur = nxt

坑3: 遍历条件混淆
  ❌ while cur.next:   # 最后一个节点进不去
  ✅ while cur:        # 每个节点都处理

坑4: 忘记返回头节点
  ❌ 函数里改了链表，但头丢了，返回不了
  ✅ 用 dummy 节点，或者始终保存 head 引用

坑5: Python 对象引用
  链表节点是对象，赋值其实是引用。node_a = node_b 改 node_a 不会影响 node_b。
  但 node_a.next = xxx 会真正改变链表结构。
"""

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ 第2课「链表」学习完成！")
    print("核心：数组 O(1) 访问，链表 O(1) 插入删除（头部）")
    print("下一步：手写反转链表 → LeetCode 206 / 21 / 141")
    print("=" * 60)

    # --- 练习题自动测试 ---
    print("\n📝 练习题测试：")

    # 测试反转链表
    test_head = make_list([1, 2, 3, 4, 5])
    result = practice_reverse_list(test_head)
    if result:
        reversed_vals = traverse(result)
        expected = [5, 4, 3, 2, 1]
        if reversed_vals == expected:
            print(f"  ✅ 练习题1 反转链表: {reversed_vals}")
        else:
            print(f"  ❌ 练习题1 预期 {expected}，实际 {reversed_vals}")
    else:
        print(f"  ⚠️  练习题1 还没写（pass了）")

    # 测试删除倒数第N个
    test_head = make_list([1, 2, 3, 4, 5])
    result = practice_remove_nth_from_end(test_head, 2)
    if result:
        result_vals = traverse(result)
        expected = [1, 2, 3, 5]
        if result_vals == expected:
            print(f"  ✅ 练习题2 删除倒数第2个: {result_vals}")
        else:
            print(f"  ❌ 练习题2 预期 {expected}，实际 {result_vals}")
    else:
        print(f"  ⚠️  练习题2 还没写（pass了）")

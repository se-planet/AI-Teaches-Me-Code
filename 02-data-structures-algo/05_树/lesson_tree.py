# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

"""
============================================================
📚 第5课：树 & 二叉树（Binary Tree）—— 数据结构最后一座大山
============================================================
学习目标：
  1. 理解二叉树的结构：根、左子树、右子树
  2. 掌握三种遍历方式：前序、中序、后序
  3. 会用递归解决树的问题
  4. 能刷 LeetCode 入门题

一句话理解：
  二叉树 = 一个有左右两个分叉的节点，每个分叉下面又可以长出一棵树。
  天然适合递归 —— 整棵树和每棵子树长得一模一样。
"""

# ============================================================
# 一、什么是二叉树？
# ============================================================
"""
树的样子：

         1         ← 根节点（root）
        / \
       2   3       ← 1 的左孩子是 2，右孩子是 3
      / \   \
     4   5   6     ← 叶子节点（没有孩子的节点）
    /
   7

术语速记：
  根节点 root   — 最上面那个
  叶子 leaf     — 没有孩子的节点（4, 5, 6, 7）
  子树 subtree  — 任何一个节点和它下面所有后代
  深度 depth    — 从根到最远叶子走了多少步
"""

# ============================================================
# 二、定义二叉树节点
# ============================================================

class TreeNode:
    """二叉树节点：一个值 + 左孩子指针 + 右孩子指针"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


# 手动造一棵树：
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(f"根节点: {root.val}")
print(f"左孩子: {root.left.val}")
print(f"右孩子: {root.right.val}")
print(f"左孩子的左孩子: {root.left.left.val}")


# ============================================================
# 三、二叉树的三种遍历（核心！）
# ============================================================
"""
          1
         / \
        2   3
       / \
      4   5

前序（根左右）：1 → 2 → 4 → 5 → 3   （先看自己，再看左右）
中序（左根右）：4 → 2 → 5 → 1 → 3   （先看左，再看自己，再看右）
后序（左右根）：4 → 5 → 2 → 3 → 1   （先看完孩子，最后看自己）

规律：前中后说的是「根」的位置。前=根在最前，中=根在中间，后=根在最后。
"""

print("\n" + "=" * 50)
print("三种遍历")
print("=" * 50)


def preorder(root):
    """前序遍历：根 → 左 → 右"""
    if not root:
        return
    print(root.val, end=" ")     # ① 打印自己
    preorder(root.left)          # ② 走左边
    preorder(root.right)         # ③ 走右边


def inorder(root):
    """中序遍历：左 → 根 → 右"""
    if not root:
        return
    inorder(root.left)           # ① 走左边
    print(root.val, end=" ")     # ② 打印自己
    inorder(root.right)          # ③ 走右边


def postorder(root):
    """后序遍历：左 → 右 → 根"""
    if not root:
        return
    postorder(root.left)         # ① 走左边
    postorder(root.right)        # ② 走右边
    print(root.val, end=" ")     # ③ 打印自己


print("前序: ", end=""); preorder(root); print()
print("中序: ", end=""); inorder(root); print()
print("后序: ", end=""); postorder(root); print()


# ============================================================
# 四、理解递归 —— 树问题的核心
# ============================================================
"""
递归就是函数自己调自己。在树上特别自然：

求一棵树有几个节点 = 1（自己）+ 左子树节点数 + 右子树节点数

这就是递归思想 —— 把大问题拆成小问题，小问题用同样方法解决。
当 root 是 None 时，返回 0（空树没有节点）。
"""


def count_nodes(root):
    """递归计算节点数"""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


print(f"\n节点数: {count_nodes(root)}")  # 5


# ============================================================
# 五、LeetCode 实战
# ============================================================

# --- LeetCode 104: 二叉树的最大深度 ---
def max_depth(root):
    """
    最大深度 = 从根到最远叶子经过的节点数
    深度 = 1（自己）+ max(左子树深度, 右子树深度)
    """
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


print(f"最大深度: {max_depth(root)}")  # 3


# --- LeetCode 226: 翻转二叉树 ---
def invert_tree(root):
    """
    翻转 = 把自己的左右孩子互换，然后递归翻转左右子树
    """
    if not root:
        return None
    root.left, root.right = root.right, root.left   # 交换左右
    invert_tree(root.left)                           # 翻左边
    invert_tree(root.right)                          # 翻右边
    return root


# 翻转前后对比
print("\n翻转前中序: ", end=""); inorder(root); print()
inverted = invert_tree(root)
print("翻转后中序: ", end=""); inorder(inverted); print()


# ============================================================
# 六、二叉搜索树（BST）—— 特殊的二叉树
# ============================================================
"""
BST 规则：左 < 根 < 右（对每个节点都成立）

      5
     / \
    3   7
   / \ / \
  2  4 6  8

BST 的好处：查找 O(log n)，像二分查找一样快。
"""


def search_bst(root, target):
    """在 BST 中查找一个值，O(log n)"""
    if not root:
        return None
    if root.val == target:
        return root
    if target < root.val:
        return search_bst(root.left, target)   # 去左边找
    else:
        return search_bst(root.right, target)  # 去右边找


# ============================================================
# 七、递归模板（背下来）
# ============================================================
"""
树的大部分问题都是这个套路：

def solve(root):
    if not root:           # 1. 空节点 → 返回
        return 0 / None / ...

    left = solve(root.left)   # 2. 递归处理左子树
    right = solve(root.right) # 3. 递归处理右子树

    return 处理(root, left, right)  # 4. 合并结果
"""

def solve(root):
    if not root:
        return 0
    
    left = solve(root.left)
    right = solve(root.right)

# ============================================================
# 八、练习题
# ============================================================

def practice_max_depth(root):
    """
    【练习题1】二叉树的最大深度（LeetCode 104）
    提示：就是 max_depth 函数，背下来
    """
    # TODO: 你的代码
    if not root:
        return 0
    left = practice_max_depth(root.left)
    right = practice_max_depth(root.right)
    return 1 + max(left, right)



def practice_is_same_tree(p, q):
    """
    【练习题2】相同的树（LeetCode 100）
    输入: 两棵树 p 和 q
    输出: True 如果结构完全相同
    提示：同时递归两棵树，每一步比较 p.val == q.val
    """
    # TODO: 你的代码
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return practice_is_same_tree(p.left, q.left) and practice_is_same_tree(p.right, q.right)


# ============================================================
# 九、常见坑
# ============================================================
"""
坑1: 忘写递归终止条件
  ❌ def f(root): return 1 + f(root.left)...
     ➜ 递归到叶子时 root.left 是 None, f(None) 里又调 f(None.left) → 死循环
  ✅ 先写 if not root: return 0

坑2: 把子树当成节点
  ❌ root.left = 5   # 应该是一个 TreeNode，不是数字
  ✅ root.left = TreeNode(5)

坑3: 混淆遍历顺序
  前序 = 根左右 → 打印自己，再走孩子
  中序 = 左根右 → 走左孩子，打印自己，走右孩子
  后序 = 左右根 → 走完孩子再打印自己
"""

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("✅ 第5课「二叉树」教程代码完成！")
    print("核心：遍历（前中后序）+ 递归（自己调自己）")
    print("下一步：手写最大深度 → LeetCode 104 / 100 / 226")
    print("=" * 60)

    # 练习题测试
    print("\n📝 练习题测试：")

    # 测试最大深度
    test_root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    result = practice_max_depth(test_root)
    if result == 3:
        print("  ✅ 练习题1 最大深度: 3")
    elif result is None:
        print("  ⚠️  练习题1 还没写")
    else:
        print(f"  ❌ 练习题1 预期 3，实际 {result}")

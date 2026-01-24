from typing import *
import collections
from collections import deque, defaultdict, Counter, OrderedDict
import random
import heapq
import bisect
import itertools
from functools import lru_cache, reduce
from math import inf, gcd, lcm, sqrt, ceil, floor, log, log2, log10
import re
import string


# Global input buffer for single word reading
class InputBuffer:
    def __init__(self):
        self.buffer = []
        self.index = 0

    def next_word(self):
        while self.index >= len(self.buffer):
            try:
                line = input().strip()
                if line:
                    self.buffer = line.split()
                    self.index = 0
                else:
                    continue
            except EOFError:
                return None

        word = self.buffer[self.index]
        self.index += 1
        return word

    def next_line(self):
        self.buffer = []
        self.index = 0
        try:
            return input().strip()
        except EOFError:
            return None


_input_buffer = InputBuffer()


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class IO:
    class Input:
        @staticmethod
        def read_bool() -> bool:
            word = _input_buffer.next_word()
            return word.lower() in ["true"] if word else False

        @staticmethod
        def read_int() -> int:
            word = _input_buffer.next_word()
            return int(word) if word else 0

        @staticmethod
        def read_float() -> float:
            word = _input_buffer.next_word()
            return float(word) if word else 0.0

        @staticmethod
        def read_string() -> str:
            return _input_buffer.next_line()

        @staticmethod
        def read_char() -> str:
            word = _input_buffer.next_word()
            return word[0] if word else ""

        @staticmethod
        def consume_newline() -> None:
            _input_buffer.next_line()

        # Array functions
        @staticmethod
        def read_int_array() -> List[int]:
            n = IO.Input.read_int()
            if n == 0:
                IO.Input.consume_newline()
            return [IO.Input.read_int() for _ in range(n)]

        @staticmethod
        def read_float_array() -> List[float]:
            n = IO.Input.read_int()
            if n == 0:
                IO.Input.consume_newline()
            return [IO.Input.read_float() for _ in range(n)]

        @staticmethod
        def read_string_array() -> List[str]:
            n = IO.Input.read_int()
            if n == 0:
                IO.Input.consume_newline()
            return [IO.Input.read_string() for _ in range(n)]

        @staticmethod
        def read_char_array() -> List[str]:
            n = IO.Input.read_int()
            if n == 0:
                IO.Input.consume_newline()
            return [IO.Input.read_char() for _ in range(n)]

        # 2D Array functions
        @staticmethod
        def read_int_2d_array() -> List[List[int]]:
            m = IO.Input.read_int()
            if m == 0:
                IO.Input.consume_newline()
            result = []
            for _ in range(m):
                row = IO.Input.read_int_array()
                result.append(row)
            return result

        @staticmethod
        def read_char_2d_array() -> List[List[str]]:
            m = IO.Input.read_int()
            if m == 0:
                IO.Input.consume_newline()
            result = []
            for _ in range(m):
                row = IO.Input.read_char_array()
                result.append(row)
            return result

        # Linked List
        @staticmethod
        def read_list_node() -> Optional[ListNode]:
            n = IO.Input.read_int()
            if n == 0:
                return None

            values = [IO.Input.read_int() for _ in range(n)]
            if not values:
                return None

            head = ListNode(values[0])
            current = head
            for i in range(1, len(values)):
                current.next = ListNode(values[i])
                current = current.next
            return head

        # Binary Tree (level-order traversal format)
        @staticmethod
        def read_tree_node() -> Optional[TreeNode]:
            n = IO.Input.read_int()
            if n == 0:
                return None

            values = []
            for _ in range(n):
                word = _input_buffer.next_word()
                if word and word.lower() == "null":
                    values.append(None)
                else:
                    values.append(int(word) if word else 0)

            if not values or values[0] is None:
                return None

            root = TreeNode(values[0])
            queue = deque([root])
            i = 1

            while queue and i < len(values):
                node = queue.popleft()

                if i < len(values):
                    if values[i] is not None:
                        node.left = TreeNode(values[i])
                        queue.append(node.left)
                    i += 1

                if i < len(values):
                    if values[i] is not None:
                        node.right = TreeNode(values[i])
                        queue.append(node.right)
                    i += 1

            return root

    class Output:
        @staticmethod
        def write_bool(x: bool) -> None:
            print("true" if x else "false", end="")

        @staticmethod
        def write_int(x: int) -> None:
            print(x, end="")

        @staticmethod
        def write_float(x: float) -> None:
            print(x, end="")

        @staticmethod
        def write_string(x: str) -> None:
            print(f'"{x}"', end="")

        @staticmethod
        def write_char(x: str) -> None:
            print(f'"{x}"', end="")

        # Array functions
        @staticmethod
        def write_int_array(arr: List[int]) -> None:
            print("[", end="")
            for i, val in enumerate(arr):
                print(val, end="")
                if i < len(arr) - 1:
                    print(",", end="")
            print("]", end="")

        @staticmethod
        def write_float_array(arr: List[float]) -> None:
            print("[", end="")
            for i, val in enumerate(arr):
                print(val, end="")
                if i < len(arr) - 1:
                    print(",", end="")
            print("]", end="")

        @staticmethod
        def write_string_array(arr: List[str]) -> None:
            print("[", end="")
            for i, val in enumerate(arr):
                print(f'"{val}"', end="")
                if i < len(arr) - 1:
                    print(",", end="")
            print("]", end="")

        @staticmethod
        def write_char_array(arr: List[str]) -> None:
            print("[", end="")
            for i, val in enumerate(arr):
                print(f'"{val}"', end="")
                if i < len(arr) - 1:
                    print(",", end="")
            print("]", end="")

        # 2D Array functions
        @staticmethod
        def write_int_2d_array(arr: List[List[int]]) -> None:
            print("[", end="")
            for i, row in enumerate(arr):
                IO.Output.write_int_array(row)
                if i < len(arr) - 1:
                    print(",", end="")
            print("]", end="")

        @staticmethod
        def write_char_2d_array(arr: List[List[str]]) -> None:
            print("[", end="")
            for i, row in enumerate(arr):
                IO.Output.write_char_array(row)
                if i < len(arr) - 1:
                    print(",", end="")
            print("]", end="")

        # Linked List
        @staticmethod
        def write_list_node(head: Optional[ListNode]) -> None:
            print("[", end="")
            first = True
            current = head
            while current:
                if not first:
                    print(",", end="")
                first = False
                print(current.val, end="")
                current = current.next
            print("]", end="")

        # Binary Tree (level-order output)
        @staticmethod
        def write_tree_node(root: Optional[TreeNode]) -> None:
            if not root:
                print("[]", end="")
                return

            print("[", end="")
            queue = deque([root])
            first = True

            while queue:
                level_size = len(queue)
                has_next_level = False

                for _ in range(level_size):
                    node = queue.popleft()

                    if not first:
                        print(", ", end="")
                    first = False

                    if node:
                        print(node.val, end="")
                        queue.append(node.left)
                        queue.append(node.right)
                        if node.left or node.right:
                            has_next_level = True
                    else:
                        print("null", end="")

                if not has_next_level:
                    break

            print("]", end="")

        # List of TreeNodes
        @staticmethod
        def write_tree_node_array(arr: List[Optional[TreeNode]]) -> None:
            print("[", end="")
            for i, tree in enumerate(arr):
                IO.Output.write_tree_node(tree)
                if i < len(arr) - 1:
                    print(",", end="")
            print("]", end="")

    # Convenience wrapper functions
    @staticmethod
    def output(x) -> None:
        if x is None:
            print("null", end="")
        elif isinstance(x, bool):
            IO.Output.write_bool(x)
        elif isinstance(x, int):
            IO.Output.write_int(x)
        elif isinstance(x, float):
            IO.Output.write_float(x)
        elif isinstance(x, str) and len(x) == 1:
            IO.Output.write_char(x)
        elif isinstance(x, str):
            IO.Output.write_string(x)
        elif isinstance(x, list):
            if x and isinstance(x[0], list):
                # 2D array
                if x[0] and isinstance(x[0][0], int):
                    IO.Output.write_int_2d_array(x)
                elif x[0] and isinstance(x[0][0], str):
                    IO.Output.write_char_2d_array(x)
                else:
                    print(x, end="")
            elif x and isinstance(x[0], int):
                IO.Output.write_int_array(x)
            elif x and isinstance(x[0], float):
                IO.Output.write_float_array(x)
            elif x and isinstance(x[0], str):
                if all(len(s) == 1 for s in x):
                    IO.Output.write_char_array(x)
                else:
                    IO.Output.write_string_array(x)
            elif x and isinstance(x[0], TreeNode):
                IO.Output.write_tree_node_array(x)
            else:
                print(x, end="")
        elif isinstance(x, ListNode):
            IO.Output.write_list_node(x)
        elif isinstance(x, TreeNode):
            IO.Output.write_tree_node(x)
        else:
            print(x, end="")


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


get = input


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        iterable = sorted(iterable)
        self.micros = [
            iterable[i : i + self.block_size - 1]
            for i in range(0, len(iterable), self.block_size - 1)
        ] or [[]]
        self.macro = [i[0] for i in self.micros[1:]]
        self.micro_size = [len(i) for i in self.micros]
        self.fenwick = FenwickTree(self.micro_size)
        self.size = len(iterable)

    def add(self, x):
        i = bisect_left(self.macro, x)
        j = bisect_right(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i : i + 1] = (
                self.micros[i][: self.block_size >> 1],
                self.micros[i][self.block_size >> 1 :],
            )
            self.micro_size[i : i + 1] = (
                self.block_size >> 1,
                self.block_size >> 1,
            )
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.bisect_right(x) - self.bisect_left(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def bisect_left(self, x):
        i = bisect_left(self.macro, x)
        return self.fenwick(i) + bisect_left(self.micros[i], x)

    def bisect_right(self, x):
        i = bisect_right(self.macro, x)
        return self.fenwick(i) + bisect_right(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return self.__class__.__name__ + (
            "({})".format(self.value) if self else "()"
        )


class LinkedList:
    def __init__(self, iterable=None):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.__len = 0
        if iterable is not None:
            self += iterable

    def get_node(self, index):
        node = self.sentinel
        i = 0
        while i <= index:
            node = node.next
            if node == self.sentinel:
                break
            i += 1
        if node == self.sentinel:
            node = None
        return node

    def __getitem__(self, index):
        node = self.get_node(index)
        return node.value

    def __len__(self):
        return self.__len

    def __setitem__(self, index, value):
        node = self.get_node(index)
        node.value = value

    def __delitem__(self, index):
        node = self.get_node(index)
        if node:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node.prev = None
            node.next = None
            node.value = None
            self.__len -= 1

    def __repr__(self):
        return str(self.to_list())

    def to_list(self):
        elts = []
        curr = self.sentinel.next
        while curr != self.sentinel:
            elts.append(curr.value)
            curr = curr.next
        return elts

    def append_node(self, node):
        self.insert_between(node, self.sentinel.prev, self.sentinel)

    def append(self, value):
        node = Node(value)
        self.insert_between(node, self.sentinel.prev, self.sentinel)

    def appendleft(self, value):
        node = Node(value)
        self.insert_between(node, self.sentinel, self.sentinel.next)

    def insert(self, index, value):
        new_node = Node(value)
        len_ = len(self)
        if len_ == 0:
            self.insert_between(new_node, self.sentinel, self.sentinel)
        elif index >= 0 and index < len_:
            node = self.get_node(index)
            self.insert_between(new_node, node.prev, node)
        elif index == len_:
            self.insert_between(new_node, self.sentinel.prev, self.sentinel)
        else:
            raise IndexError

    def insert_between(self, node, left_node, right_node):
        if node and left_node and right_node:
            node.prev = left_node
            node.next = right_node
            left_node.next = node
            right_node.prev = node
            self.__len += 1
        else:
            raise IndexError

    def insert_after(self, node, value):
        new_node = Node(value)
        node.next.prev = new_node
        new_node.next = node.next
        node.next = new_node
        new_node.prev = node
        self.__len += 1

    def merge_left(self, other):
        self.sentinel.next.prev = other.sentinel.prev
        other.sentinel.prev.next = self.sentinel.next
        self.sentinel.next = other.sentinel.next
        self.sentinel.next.prev = self.sentinel
        self.__len += other.__len

    def merge_right(self, other):
        self.sentinel.prev.next = other.sentinel.next
        other.sentinel.next.prev = self.sentinel.prev
        self.sentinel.prev = other.sentinel.prev
        self.sentinel.prev.next = self.sentinel
        self.__len += other.__len

    def pop(self, node=None):
        if node is None:
            node = self.sentinel.prev
        if self.__len < 1:
            raise IndexError
        node.prev.next = node.next
        node.next.prev = node.prev
        self.__len -= 1
        return node.value

    def before(self, node):
        return node.prev.prev if node.prev == self.sentinel else node.prev

    left = before
    prev = before

    def after(self, node):
        return node.next.next if node.next == self.sentinel else node.next

    right = after
    next = after


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        return 1


def main():
    t = IO.Input.read_int()
    for _ in range(t):
        grid = IO.Input.read_int_2d_array()
        k = IO.Input.read_int()
        solution = Solution()
        result = solution.maxPathScore(grid, k)
        IO.output(result)
        print()


if __name__ == "__main__":
    main()

from typing import List
from collections import deque

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        n = len(parent)
        self.locked = [-1] * n
        self.children = [[] for _ in range(n)]
        for i in range(1, n):
            self.children[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] == -1:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        # Condition 1: The node must be unlocked.
        if self.locked[num] != -1:
            return False

        # Condition 2: It must not have any locked ancestors.
        p = self.parent[num]
        while p != -1:
            if self.locked[p] != -1:
                return False
            p = self.parent[p]

        # Condition 3: It must have at least one locked descendant.
        # We perform this check without modifying the tree.
        locked_descendant_found = False
        q = deque(self.children[num])
        while q:
            node = q.popleft()
            if self.locked[node] != -1:
                locked_descendant_found = True
                break  # Found one, no need to check further
            q.extend(self.children[node])
        
        if not locked_descendant_found:
            return False

        # --- All conditions met, now perform the state change ---

        # Action 1: Unlock all descendants.
        q_unlock = deque(self.children[num])
        while q_unlock:
            node = q_unlock.popleft()
            self.locked[node] = -1  # Unlock the descendant
            q_unlock.extend(self.children[node])

        # Action 2: Lock the target node.
        self.locked[num] = user
        return True
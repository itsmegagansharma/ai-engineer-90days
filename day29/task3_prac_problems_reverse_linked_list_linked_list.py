"""
Day 29 · Task 3 · Practice: Problems: Reverse Linked List & Linked List Cycle

Solve both in the starter file, then run it: every assert must pass.

Complete every TODO, run the file, then tick this task on the tracker.
"""
# ---------------- Reverse Linked List ----------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse the list by re-pointing .next. Keep prev and current."""
    pass


# ---------------- Linked List Cycle ----------------
def has_cycle(head) -> bool:
    """Floyd's tortoise and hare: a slow and a fast pointer. Reuse ListNode from the problem above."""
    pass


if __name__ == "__main__":
    # Reverse Linked List
    assert to_list(reverse_list(build([1, 2, 3, 4]))) == [4, 3, 2, 1]
    # Linked List Cycle
    a = ListNode(1); b = ListNode(2); c = ListNode(3); a.next = b; b.next = c; c.next = b
    assert has_cycle(a)
    assert not has_cycle(build([1, 2, 3]))
    print("All tests passed!")

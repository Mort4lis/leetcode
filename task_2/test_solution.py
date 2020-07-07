from .solution import ListNode, add_two_number
import pytest


def to_number(linked_list: ListNode):
    mul = 1
    result = 0
    while linked_list:
        result += linked_list.val * mul
        linked_list = linked_list.next
        mul *= 10
    return result


@pytest.mark.parametrize(['l1', 'l2'], [
    [
        ListNode(2, ListNode(4, ListNode(3))),
        ListNode(5, ListNode(6, ListNode(4))),
    ],
    [
        ListNode(0, ListNode(1)),
        ListNode(0, ListNode(1, ListNode(2))),
    ],
    [
        None,
        ListNode(0, ListNode(1))
    ],
    [
        ListNode(9, ListNode(9)),
        ListNode(1)
    ]
])
def test_add_two_number(l1: ListNode, l2: ListNode):
    num1 = to_number(l1)
    num2 = to_number(l2)
    result = add_two_number(l1, l2)
    assert num1 + num2 == to_number(result)

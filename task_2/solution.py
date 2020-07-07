class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_number(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Даны два списка, где каждый элемент этого списка - число (от 0 до 9).
    Вернуть результирующий список, который равен сумме данных двух списков.

    Пример:
    l1 = 2 -> 4 -> 3 (==342)
    l2 = 5 -> 6 -> 4 (==465)
    res = 7 -> 0 -> 8 (==807)

    Args:
        l1: первый список
        l2: второй список

    Returns: результирующий список, равный сумме двух списков l1 и l2

    """
    head = ListNode()
    curr = head
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        digit = x + y + carry
        carry = digit // 10

        curr.next = ListNode(digit % 10)
        curr = curr.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)

    if carry > 0:
        curr.next = ListNode(carry)

    return head.next

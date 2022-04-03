# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item

#     def __str__(self):
#         return self.value


def solution(head, elem):
    current_idx = 0
    current_elem = head
    while current_elem:
        if current_elem.value == elem:
            return current_idx
        current_elem = current_elem.next_item
        current_idx += 1
    return -1


# def test():
#     node3 = Node("node3", None)
#     node2 = Node("node2", node3)
#     node1 = Node("node1", node2)
#     node0 = Node("node0", node1)
#     idx = solution(node0, "node2")
#     print(idx)
#     # result is idx == 2


# test()

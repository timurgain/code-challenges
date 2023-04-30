"""Deleting a linked list item."""


# # Comment it before submitting
# class Node:  
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item
    
#     def __str__(self):
#         return self.value


def solution(head, idx):

    current_node = head
    current_id = 0
    previous_node = None

    while current_node:
        if current_id == idx:
            if previous_node:
                previous_node.next_item = current_node.next_item
            else:
                head = head.next_item
                return head

        previous_node = current_node
        current_node = current_node.next_item
        current_id += 1

    return head


# def test():
#     node3 = Node("node3", None)
#     node2 = Node("node2", node3)
#     node1 = Node("node1", node2)
#     node0 = Node("node0", node1)
#     new_head = solution(node0, 1)
#     print(new_head)
# #     # result is node0 -> node2 -> node3


# test()

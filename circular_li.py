class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_circular_linked_list():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node1  
    return node1


head = create_circular_linked_list()


current = head
for _ in range(6):
    print(current.data)
    current = current.next










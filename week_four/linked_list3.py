class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# def iter_linked_list(node):
#     while node is not None:
#         print(node.value)
#         node = node.next
        
        
# head = Node("1st Node")
# head.next = Node("2nd Node")
# head.next.next= Node("3rd Node") 
# head.next.next.next= Node("4th Node") 
# head.next.next.next.next= Node("The last Node") 
# # print(head.value)
# # pr  int(head.next.value)
# # print(head.next.next.value)
# iter_linked_list(head)
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            print("Head Node created", self.head.value)
            return
        
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        print("Appended new Node with value:", node.next.value)
        
llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
        
        
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def display_nodes(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# Create a linked list with 5 nodes
linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)

# Display the nodes
linked_list.display_nodes()'''


stack=[]
s=input()
n=len(s)
c=0
flag=1
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
else:
    for i in range(n):
        if s[i]=='[' or s[i]=='(' or s[i]=='{':
            stack.append(s[i])
            c+=1
        elif s[i]==']' or s[i]=='}' or s[i]==')':
            if stack==[]:
                flag=0
                break
            if (stack[-1]=='{' and s[i]=='}') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='(' and s[i]==')'):
                stack.pop()
                c-=1
            else:
                flag=0
                break
        else:
            flag=-1
            break
    if flag==0 or c!=0:
        print(False)
    elif flag==-1:
        print("Invalid Paranthesis")
    else:
        print(True)

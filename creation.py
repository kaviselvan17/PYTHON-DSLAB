class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def insertAfer(self,previous_node,new_data):
        if (previous_node is None):
            print("the given previous node must in linked list")
            return
        new_node=Node(new_data)
        new_node.next=previous_node.next
        previous_node.next=new_node
    def append(self,new_node):
        new_node=Node(new_node)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
            last.next=new_node
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=='main':
    llist=LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.insertAfter(llist.head.next,8)
    print("created linked list is:")
    llist.printlist()


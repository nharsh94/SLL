# Node implementation for a singly-linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data;
        self.next = next;

# Singly Linked List implementation
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    # Adds to the end of a Linked List    
    def add(self, data):
        # If nothing in Linked List
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            return "Set new head"
            
        pointer = self.head
        while(pointer.next != None):
            pointer = pointer.next
            
        pointer.next = Node(data)
        return "Added to end of the list"
        
    # Search for data in the LL and delete the node 
    
    def delete(self, data_to_delete):
        if self.head == None:
            print("Nothing to delete")
            return 
        
        prev = None
        curr = self.head
        # Loop through list to find data to delete
        while curr != None:
            if curr.data == data_to_delete:
                # First node
                if curr == self.head:
                    return "Deleted the first node"
                # last node
                elif curr.next == None:
                    prev.next = None
                    return "Deleted the last node"
                # middle node
                else:
                    prev.next = curr.next
                    return "Deleted in the middle of the list"
                    
            prev = curr
            curr = curr.next
            
        print("Nothing to delete")
            
    def printList(self):
        pointer = self.head
        while(pointer):
            print(pointer.data, end="-->")
            pointer = pointer.next

if __name__ == '__main__':
    list = LinkedList()
    list.add(1)
    list.add(2)
    list.add(3)
    list.add(4)
    list.printList()
    print("\nList after delete")
    list.delete(3)
    list.printList()

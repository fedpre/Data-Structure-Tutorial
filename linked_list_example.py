"""
Example Problem Linked Lists
How to Reverse a List
"""

class LinkedList:
    """
    LinkedList class to implement the data structure. The purpose of this example is to show how to reverse a Linked List
    """
    class Node:
        """
        Create the structure for a Node
        """
        def __init__(self, data):
            """
            Initialized the Node to the data provided
            """
            self.data = data
            self.next = None
            self.prev = None
        
    def __init__(self):
        """
        Initiliaze an empty linked list
        """
        self.head = None
        self.tail = None
        self.reversed_list = list()
    
    def insert_head(self, value):
        """
        Insert a new Node as the head of the list
        """
        new_node = LinkedList.Node(value)

        # Case 1 - List is empty
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        # Case 2 - List is not empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, value):
        """
        Insert a new Node at the tail of the list
        """
        new_node = LinkedList.Node(value)

        # Case 1 - List is empty
        if self.tail == None and self.head == None:
            self.head = new_node
            self.tail = new_node

        # Case 2 - List is not empty
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def insert_after(self, value):
        """
        Insert new_value after the occurrence of value in the linked list
        """
        # Start searching at the head of the list
        current = self.head
        while current is not None:
            if current.data == value:
                # Check if the value is the tail
                # If so user the 'insert_tail() method'
                if current == self.tail:
                    self.insert_tail(value)
                # Insert the value in the middle of the list
                else:
                    new_node = LinkedList.Node(value)
                    new_node.prev = current
                    new_node.next = current.next
                    current.next.prev = new_node
                    current.next = new_node
                return
            # Check the next value in the list
            current = current.next
    
    def rev_l(self):
        """
        Return the reversed linked list
        """
        # Set the current Node to the tail
        current = self.tail
        
        # Iterate over the list from the tail to the head
        while current is not None:
            # Append the value to the list
            self.reversed_list.append(current.data)
            # Set current to the previous node
            current = current.prev

        # Return the list
        return self.reversed_list
    def __str__(self):
        """
        Returns a string representation of the object
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
    def __iter__(self):
        """
        Iterate forward through the Linked List
        """
        # Start at the beginning of the list
        current = self.head
        # Iterate over the entire link
        while current != None:
            # Provide or give each item to the user
            yield current.data
            # Go to the next Node
            current = current.next


# Test Cases
my_ll = LinkedList()
my_ll.insert_head(9) 
my_ll.insert_head(7) 
my_ll.insert_head(5) 
my_ll.insert_tail(3) 
my_ll.insert_tail(1) 
my_ll.insert_tail(0) 
print(my_ll)
print(my_ll.rev_l())

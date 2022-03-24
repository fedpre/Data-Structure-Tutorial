# Initialize the Printer class
class Printer():
    """
    The Printer class allow users to enter a queue to print a document.
    It is implemented following the FIFO method to process the requests.
    """
    class Node():
        """
        Each Node in the queue will have a value (the document to print) assigned to it and the user who sent the document.
        """
        def __init__(self, document, user):
            self.value = document
            self.user = user
        
        def __str__(self):
            """
            Graphical representation of the node
            """
            return "Document: {} sent from {}".format(self.value, self.user)

    def __init__(self):
        """
        Initialize an empty queue
        """
        self.queue = []

    def enqueue_document(self, value, user):
        """
        Add a new Node at the back of the queue with a value and a user.attached. The Node will always be added at the back of the queue.
        """
        new_node = Printer.Node(value, user)
        self.queue.append(new_node)

    def dequeue_documents(self):
        """
        Dequeue all the elements, starting from the first. 
        Print all the documents until the queue is empty
        """
        # Check if the queue is empty
        if len(self.queue) == 0:
            print("There are no documents in the printer queue")
            return None

        while len(self.queue) != 0:
            item_to_print = self.queue.pop(0)
            print(f"\nPrinting item {item_to_print.value} from user {item_to_print.user}")
            print("Printing complete... Ready to print next item")

        if len(self.queue) == 0:
            print("\nPrinting complete. The queue is empty.")

    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """
        Suppport the str() function to provide a string representation of the queue.
        """
        string = "["
        for node in self.queue:
            string += str(node)  # This uses the __str__ from the Node class
            string += ", "
        string += "]"
        return string

# Test cases
printer_queue = Printer() # Create the Printer object
printer_queue.enqueue_document('text1.txt', 'Anne') # Add a document to the queue
printer_queue.enqueue_document('text2.txt', 'Bob')  # Add a document to the queue
printer_queue.enqueue_document('text3.txt', 'Charlie')  # Add a document to the queue
print(printer_queue) # [Document: text1.txt sent from Anne, Document: text2.txt sent from Bob, Document: text3.txt sent from Charlie, ]
printer_queue.dequeue_documents() # Print all the documents in the queue
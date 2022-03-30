class FamilyTree():
    """
    Initialize a new Family Tree. When created, a new family tree gets the name of the first person on the tree.
    """
    class Person():
        """
        Create a new person object. The new person object accepts as parameters a name and a birthday
        """
        def __init__(self, name, birthday):
            """
            Create the person object providing name and birthday
            """
            self.name = name
            self.birthday = birthday
            self.right = None
            self.left = None

        def change_name(self, name:str):
            """
            Set a new name for a person
            """
            self.name = name
            return self.name

        def change_birthday(self, birthday:str):
            """
            Set a new birthday for a person
            """
            self.birthday = birthday
            return self.birthday

        def __str__(self):
            return "[name: {}, birthday: {}], ".format(self.name, self.birthday)


    def __init__(self, name:str, birthday:str):
        """
        Initialize a new Family Tree with the first person of the tree
        """
        self.root = FamilyTree.Person(name, birthday)

    
    def insert(self, name:str, birthday:str):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = FamilyTree.Person(name, birthday)
        else:
            self._insert(name, birthday, self.root)  # Start at the root


    def _insert(self, name:str, birthday:str, node):
        """
        This function will look for a place to insert a node
        with the name and birthday inside of it.
        """
        if node == None:
            return
        
        if name < node.name:
            if node.left is None:
                # We found an empty spot
                node.left = FamilyTree.Person(name, birthday)
            else:
                self._insert(name, birthday, node.left)

        elif name > node.name:
            if node.right is None:
                # We found an empty spot
                node.right = FamilyTree.Person(name, birthday)
            else:
                self._insert(name, birthday, node.right)


    def get_generations(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_generations on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_generations(self.root)  # Start at the root


    def _get_generations(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_generations.
        """
        # Base case
        if node is None:
            return 0
        # Search the left side of the tree 
        left_sub = self._get_generations(node.left)
        # Search the right side of the tree 
        right_sub = self._get_generations(node.right)

        # return the max between the two adding the root node
        return max(left_sub, right_sub) + 1

  
    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
        the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
    
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.name
            yield from self._traverse_forward(node.right)


# Test cases
family_tree = FamilyTree('Federico', '07/10/1992')
family_tree.insert('Luca', '02/05/1963')
family_tree.insert('Livia', '12/04/1963')
family_tree.insert('Carlo', '02/05/1963')
family_tree.insert('Rita', '12/04/1963')
family_tree.insert('Alessandra', '02/05/1963')
family_tree.insert('Luciano', '12/04/1963')

print(family_tree.get_generations())
for person in family_tree:
    print(person)
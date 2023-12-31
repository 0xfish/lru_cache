"""
LRU Cache data structure.

A generic LRU cache data structure. The DS must be initialized to a positive integer size.
"""
class Node:
    """
    Doubly linked list Node data structure.
    """
    def __init__(self, key, value):
        """
        Initializes doubly linked list data structure.

        Args:
            key: Any python object.
            value: Any python object.

        Returns: 
            None

        Raises:
            Nothing
        """
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class lru_cache:
    """
    Cache uses a doubly linked list and dictionary to achieve an O(1) for get/set methods.

    The doubly linkedlist keeps the ordering, while the dictionary gives a random access to the nodes on the linkedlist.
    """
    def __init__(self, size):
        """
        Initializes the LRU cache data structure.

        Args:
            size: Positve integer size of cache.

        Returns: 
            None

        Raises:
            Assertion for a positive size.
        """
        assert type(size) == int, "ERROR: %s is not an integer" % (size.__str__)
        assert size > 0, "ERROR: %s is not a positive integer" % (size.__str__)
        # Make dummy nodes
        self.head = Node(0,0) 
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # Initialize general data members
        self.data = {}
        self.size = size
    def __insert(self, node: Node) -> None:
        """
        Insert node at the end of the doubly linked list.

        Args:
            node: Doubly linked list Node.

        Returns: 
            None

        Raises:
            Nothing.
        """
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        self.tail.prev = node
        node.next = self.tail

    def __remove(self, node: Node) -> None:
        """
        Remove from doubly linked list.

        Args:
            node: Doubly linked list Node.

        Returns: 
            None

        Raises:
            Nothing.
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def __evict(self) -> None:
        """
        Pop from the head of doubly linked list.

        Args:
            Nothing.

        Returns: 
            None

        Raises:
            Python dictionary key error.
        """
        temp = self.head.next

        assert temp.key in self.data, "ERROR: Key: %s is not in Cache" % (temp.key.__str__)

        self.__remove(temp)      
        self.data.pop(temp.key)
    def contains(self, key) -> bool:
        """
        Returns a boolean on whether key is in cache.

        Args:
            key: Any python object.

        Returns: 
            Bool 

        Raises:
            Nothing
        """
        return True if key in self.data else False
    
    def get(self, key):
        """
        Return value from key.

        Args:
            key: Any python object.

        Returns: 
            value from key if it exists

        Raises:
            Python dictionary key error.
        """
        assert key in self.data, "ERROR: Key: %s is not in Cache" % (key.__str__)

        temp = self.data[key]
        self.__remove(temp)
        self.__insert(temp)
        return temp.value

    def put(self, key, value) -> None:
        """
        Insert key value pair into data structure.

        Args:
            key: Any python object.
            value: Any python object

        Returns: 
            None

        Raises:
            Nothing.
        """
        # Reorder the sequence to reflect update.
        if key in self.data:
            self.__remove(self.data[key])
        # Insert into dictionary and linkedlist.     
        self.data[key] = Node(key, value)
        self.__insert(self.data[key])
        # If reached limit, evict a line from cache.
        if len(self.data) > self.size:
            self.__evict()
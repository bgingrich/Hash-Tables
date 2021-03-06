class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__ (self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
    
    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for i in key:
            hash = ((hash << 5) + hash) + ord(i)
            hash &= 0xffffffff
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        new_pair = HashTableEntry(key, value)

        loadFactor = self.size() / self.capacity
        if loadFactor > 0.7:
            self.resize()

        node = self.storage[index]
        if node is None:
            self.storage[index] = new_pair
            return
        
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            prev.next = new_pair
        
        else:
            node.value = value

        loadFactor = self.size() / self.capacity
        if loadFactor > 0.7:
            self.resize()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]
        
        if node.key == key:
            self.storage[index] = node.next
            return
        
        while node is not None and node.key != key:
            prev = node
            node = node.next
        
        if node is None:
            print("f{key} not found")
            return None

        loadFactor = self.size() / self.capacity
        if loadFactor > 0.7:
            self.resize()
        
        prev.next = node.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.storage[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        
        else:
            return node. value

    def size(self):
        size = 0
        for i in self.storage:
            r = i
            while r is not None:
                size += 1
                if r.next is None:
                    break
                else:
                    r = r.next
        return size

    def resize(self, new_capacity=None):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        if new_capacity is not None:
            self.capacity = new_capacity
        else:
            self.capacity = self.capacity * 2
        
        tempStorage = self.storage

        self.storage = [None] * self.capacity

        for i in tempStorage:
            r = i

            while r is not None:
                prev = r
                r = prev.next
                prev.next = None

                self.put(prev.key, prev.value)
        


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")

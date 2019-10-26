"""Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class Node:
    def __init__(self,key,val):
        self.key = key
        self.value = val
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self,capacity):
        self.capacity = capacity -1
        # Element to be evicted next if it is not referenced next
        self.start = None
        # Most recent element inserted.
        self.tail = None
        self.cache = dict()

    def get(self, key):

        if key in self.cache:
            node_address = self.cache[key]
            self.delete_node(node_address)
            self.add_node_to_the_top(node_address)

            return node_address.value

        return -1

    def add_node_to_the_top(self, node):

        if self.start is None:
            self.start = node
            self.tail = self.start

        else:
            node.left = self.tail
            node.right = None
            self.tail.right = node
            self.tail = node

        return

    def delete_node(self, node):

        if node.left:
            node.left.right = node.right
        else:
            self.start = node.right

        if node.right:
            node.right.left = node.left
        else:
            self.tail = node.left

        return

    def put(self,key,value):

        if key in self.cache:
            node_address = self.cache[key]
            node_address.value = value

            self.delete_node(node_address)
            # Add it to the top of the frame , since it has been accessed currently

            self.add_node_to_the_top(node_address)

        else:

            node = Node(key, value)
            curr_window_size = len(self.cache)

            if curr_window_size > self.capacity:
                print(self.tail.key)
                # Now since the current window size is grater than window size, now pop least used one
                self.cache.pop(self.start.key)
                self.delete_node(self.start)
                self.add_node_to_the_top(node)

            else:

                self.add_node_to_the_top(node)

            self.cache[key] = node

    def print_cache(self):
        temp = self.start
        while temp:
            print("Key:{0}  Val:{1}".format(temp.key,temp.value))
            temp = temp.right


if __name__ == "__main__":

    cache = LRUCache(4)

    cache.put(1,1)
    cache.put(2,2)
    cache.put(3,3)
    cache.put(4,4)
    cache.put(5,5)

    cache.get(3)
    print(cache.print_cache())
    cache.get(2)
    print(cache.print_cache())

    cache.put(6,6)
    cache.get(5)
    cache.put(7,7)
    print(cache.print_cache())

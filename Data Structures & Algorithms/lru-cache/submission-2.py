class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.c_map = {}

        # dummy left and right nodes
        self.left = Node()   # LRU side
        self.right = Node()  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def add(self, node):
        # add right before self.right
        prev_node = self.right.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.c_map:
            return -1

        node = self.c_map[key]

        # mark as recently used
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.c_map:
            node = self.c_map[key]
            node.val = value

            self.remove(node)
            self.add(node)
        else:
            node = Node(key, value)
            self.c_map[key] = node
            self.add(node)

        if len(self.c_map) > self.capacity:
            # remove least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.c_map[lru.key]
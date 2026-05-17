class Node():
    def __init__(self, key, value):
        self.key: int = key
        self.value: int = value
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = {}
        self.head = Node(key=-1, value=-1)  # most recently used
        self.tail = Node(key=-1, value=-1)  # least recently used
        self.head.next, self.tail.prev = self.tail, self.head  # CHECKED

    def remove_node(self, node: Node):
        p, n = node.prev, node.next
        if p:
            p.next = n
        if n:
            n.prev = p

    def add_to_mru(self, node: Node):  # most recently used
        next_ = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = next_
        if next_:
            next_.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_mru(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_to_mru(node)
            return

        node = Node(key, value)
        if len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            if lru_node:
                self.remove_node(lru_node)
                del self.cache[lru_node.key]

        self.add_to_mru(node)
        self.cache[key] = node

class Node:
    """Node in the doubly linked list for each frequency"""

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1  # All nodes start with frequency 1
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly linked list to manage nodes with the same frequency"""

    def __init__(self):
        self.head = Node(-1, -1)  # dummy head
        self.tail = Node(-1, -1)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node: Node):
        """Add node right after the dummy head (most recent position)"""
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
        self.size += 1

    def remove_node(self, node: Node):
        """Remove a specific node from the list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def remove_tail(self) -> Node:
        """Remove and return the node before dummy tail (least recent)"""
        if self.size == 0:
            return None
        tail_node = self.tail.prev
        self.remove_node(tail_node)
        return tail_node


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0  # Track the current minimum frequency
        self.key_to_node = {}  # key -> Node
        self.freq_to_list = {}  # freq -> DoublyLinkedList

    def _update_frequency(self, node: Node):
        """Helper method to update node's frequency when accessed"""
        # Remove node from its current frequency list
        old_freq = node.freq
        old_list = self.freq_to_list[old_freq]
        old_list.remove_node(node)

        # If this frequency list becomes empty and it was the min_freq, increment min_freq
        if old_list.size == 0 and old_freq == self.min_freq:
            self.min_freq += 1

        # Increase node's frequency
        node.freq += 1

        # Add node to its new frequency list
        new_freq = node.freq
        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()

        new_list = self.freq_to_list[new_freq]
        # Add to head (most recent for this frequency)
        new_list.add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node or self.capacity == 0:
            return -1

        node = self.key_to_node[key]
        self._update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        # If key exists, update value and frequency
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update_frequency(node)
            return

        # If capacity is full, evict the LFU (least frequent + least recent)
        if len(self.key_to_node) == self.capacity:
            # Get the list for the current minimum frequency
            lfu_list = self.freq_to_list[self.min_freq]
            # Remove the node before tail (least recently used among LFU items)
            node_to_remove = lfu_list.remove_tail()
            if node_to_remove:
                del self.key_to_node[node_to_remove.key]

        # Create new node
        new_node = Node(key, value)
        new_node.freq = 1
        self.key_to_node[key] = new_node

        # Add to frequency list for freq = 1
        if 1 not in self.freq_to_list:
            self.freq_to_list[1] = DoublyLinkedList()

        freq_1_list = self.freq_to_list[1]
        freq_1_list.add_to_head(new_node)

        # Reset min_freq to 1 for new node
        self.min_freq = 1

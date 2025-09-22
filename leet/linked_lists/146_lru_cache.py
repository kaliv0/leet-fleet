# 146. LRU Cache


class DoublyListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        """Initialize the LRU cache with positive size capacity."""
        self.capacity = capacity
        self.kv_map = {}

        self.dl_list = DoublyListNode()
        self.head = self.dl_list
        self.tail = self.dl_list

    def get(self, key: int) -> int:
        """Return the value of the key if the key exists, otherwise return -1."""
        if key not in self.kv_map:
            return -1

        node = self.kv_map[key]
        self._move_node_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
            If the number of keys exceeds the capacity from this operation, evict the least recently used key."""
        if key in self.kv_map:
            # update val
            self.kv_map[key].val = value
            # move to front
            node = self.kv_map[key]
            self._move_node_to_front(node)
        else:
            # create and attach new node
            new_node = DoublyListNode(key, value)
            self.head.next = new_node
            new_node.prev = self.head
            # move head
            self.head = self.head.next
            # add to dict for fast retrieval
            self.kv_map[key] = new_node

            # check capacity and evict oldest if needed
            if len(self.kv_map) > self.capacity:
                # detach node form tail
                node_to_evict = self.tail.next
                node_to_evict.prev.next = node_to_evict.next
                node_to_evict.next.prev = node_to_evict.prev
                # delete node from kv_map by node.key
                del self.kv_map[node_to_evict.key]

    def _move_node_to_front(self, node):
        if self.head != node:
            # detach node from inside dl_list
            node.prev.next = node.next
            node.next.prev = node.prev
            # move to in front
            self.head.next = node
            node.prev = self.head
            node.next = None
            # move head
            self.head = self.head.next


if __name__ == "__main__":
    ops_cases = [
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        ["LRUCache", "put", "get"],
        ["LRUCache", "put", "put", "put", "put", "get", "get"]
    ]
    vals_cases = [
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
        [[1], [2, 1], [2]],
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
    ]

    for ops, vals in zip(ops_cases, vals_cases):
        obj = LRUCache(capacity=vals[0][0])
        for i in range(1, len(ops)):
            print(getattr(obj, ops[i])(*vals[i]))
            print(f"{ops[i]}, {vals[i]}")
            print({(k, v.val) for k, v in obj.kv_map.items()})
            print("======================")

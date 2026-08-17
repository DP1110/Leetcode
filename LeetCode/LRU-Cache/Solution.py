1class Node(object):
2    def __init__(self, key, val):
3        self.key = key
4        self.val = val
5        self.prev = None
6        self.next = None
7
8
9class LRUCache(object):
10    def __init__(self, capacity):
11        self.cap = capacity
12        self.map = {}
13        self.head = Node(0, 0)  # dummy
14        self.tail = Node(0, 0)  # dummy
15        self.head.next = self.tail
16        self.tail.prev = self.head
17
18    def _remove(self, node):
19        node.prev.next = node.next
20        node.next.prev = node.prev
21
22    def _add_to_end(self, node):
23        # insert right before tail (most recent)
24        p = self.tail.prev
25        p.next = node
26        node.prev = p
27        node.next = self.tail
28        self.tail.prev = node
29
30    def get(self, key):
31        if key not in self.map:
32            return -1
33        node = self.map[key]
34        self._remove(node)
35        self._add_to_end(node)
36        return node.val
37
38    def put(self, key, value):
39        if key in self.map:
40            node = self.map[key]
41            node.val = value
42            self._remove(node)
43            self._add_to_end(node)
44        else:
45            node = Node(key, value)
46            self.map[key] = node
47            self._add_to_end(node)
48            if len(self.map) > self.cap:
49                lru = self.head.next
50                self._remove(lru)
51                del self.map[lru.key]
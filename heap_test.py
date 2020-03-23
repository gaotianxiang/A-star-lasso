import heapq


class Node:
    def __init__(self, *args):
        self.a = args
        print(self.a)

    def __lt__(self, other):
        return sum(self.a) < sum(other.a)

    def __repr__(self):
        return ' '.join([str(x) for x in self.a])

    def __hash__(self):
        return repr(self).__hash__()


na = Node(2, 3, 4)
nb = Node(2, 1, 6)
nc = Node(2, 3, 4)
print(nc.__hash__() == na.__hash__())
# print(na < nb)

a = []
# heapq.heapify(a)

heapq.heappush(a, Node(2, 3, 4))
heapq.heappush(a, Node(1, 2))

print(a)

from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def __repr__(self):
        return f"Lista({list(self._data)})"

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        try:
            return self._data.popleft()
        except IndexError:
            raise IndexError('lista vazia') from None

    def search(self, index):
        if not 0 <= index <= len(self._data) - 1:
            raise IndexError

        return self._data[index]

    def is_empty(self):
        return not bool(len(self._data))

    def size(self):
        return len(self._data)

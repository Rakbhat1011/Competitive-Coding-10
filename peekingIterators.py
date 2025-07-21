"""
Wrap the original iterator and always cache the next element
peek() just returns the cached value
next() returns the cached value and preloads the next one
"""
"""
Time Complexity : O(1) Returns the cached _next value
Space Complexity : O(1) Only one element is cached (self._next)
"""

class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def hasNext(self):
        return self.index < len(self.nums)

    def next(self):
        if self.hasNext():
            val = self.nums[self.index]
            self.index += 1
            return val
        raise StopIteration()

class PeekingIterator:
    def __init__(self, iterator: 'Iterator'):
        self.iterator = iterator
        self._next = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self) -> int:
        return self._next

    def next(self) -> int:
        current = self._next
        self._next = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self) -> bool:
        return self._next is not None


if __name__ == "__main__":
    it = Iterator([1, 2, 3])
    peekIt = PeekingIterator(it)

    print(peekIt.peek()) 
    print(peekIt.next())
    print(peekIt.peek()) 
    print(peekIt.next()) 
    print(peekIt.hasNext())  
    print(peekIt.next())
    print(peekIt.hasNext()) 

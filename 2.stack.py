
class Stack(object):
    __slots__ = ('__items',)

    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def size(self):
        return len(self.__items)

    def peek(self):
        return self.__items[self.size() - 1]

    def push(self,item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

if __name__ == '__main__':
    s = Stack()
    s.push('h')
    s.push('a')
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.peek())

    print(s.size())
    print(s.pop())
    print(s.size())

    print(s.is_empty())

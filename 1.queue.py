class Queue(object):

    def __init__(self):
        self.queue = []

    def in_queue(self,*args):
        self.queue.extend(args)

    def out_queue(self):
        if not self.queue == []:
            self.queue.pop(0)
        else:
            return None

    def show(self):
        for item in self.queue:
            print(item)

    def head(self):
        if not self.queue == []:
            return self.queue[0]
        else:
            return None

    def tail(self):
        if not self.queue == []:
            return self.queue[-1]
        else:
            return None

    def is_empty(self):
        return self.queue == []

    def length(self):
        return len(self.queue)

if __name__ == '__main__':
    q =Queue1()
    q.in_queue(1)
    q.show()

    q.in_queue(2,3,4,5)
    q.show()

    q.out_queue()
    q.show()

    print(q.head())
    print(q.tail())

    print(q.length())
    print(q.is_empty())
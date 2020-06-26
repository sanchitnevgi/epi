from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    SCALE_FACTOR = 2
    def __init__(self, capacity: int) -> None:
        self.entries = [None] * capacity
        self.head = self.tail = self.num_elements = 0
    
    def enqueue(self, x: int) -> None:
        # If the queue is full
        if self.num_elements == len(self.entries):
            # Make the entries contiguous
            self.entries = self.entries[self.head:] + self.entries[:self.head]

            # Increase the capacity
            self.entries += [None] * (len(self.entries) * Queue.SCALE_FACTOR - len(self.entries))

            # Reset the head, tail
            self.head, self.tail = 0, self.num_elements


        self.entries[self.tail] = x
        self.tail = (self.tail + 1) % len(self.entries)
        self.num_elements += 1

    def dequeue(self) -> int:
        self.num_elements -= 1
        result = self.entries[self.head]
        self.head = (self.head + 1) % len(self.entries)

        return result

    def size(self) -> int:
        return self.num_elements    


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))

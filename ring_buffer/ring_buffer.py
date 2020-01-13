from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        ring_length = len( self.get() )

        if ring_length < self.capacity:
            self.storage.add_to_tail( item )

            if ring_length == 0:
                self.current = self.storage.tail

        else:
            self.current.value = item

            if self.current.next is not None:
                self.current = self.current.next
            else:
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.storage.head is not None:
            current = self.storage.head

            list_buffer_contents.append(current.value)

            while current.next is not None:
                current = current.next

                list_buffer_contents.append(current.value)

            return list_buffer_contents
        else:
            return []

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print( buffer.get() )   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print( buffer.get() )   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

print( buffer.get() )   # should return ['d', 'e', 'f']

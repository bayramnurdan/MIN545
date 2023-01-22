# MIN 545 HW 5 Nurdan Emin
# 2143139
"""Please add a reverse method to the LinkedList class which will reverse the linked list. There are two conditions:

The method should take at most O( n ) steps, n being the number of items in the list
The method must work in-place; meaning you are not allowed to create new linked lists or even new ListNodes,
 your method can only arrange the links of existing nodes."""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def insert(self, new_value):
        self.next = ListNode(new_value, self.next)


class LinkedList:
    def __init__(self, initial_data=None):
        self.head = None
        if initial_data is not None:
            for item in reversed(initial_data):
                self.push(item)

    def push(self, newval):
        self.head = ListNode(value=newval, next=self.head)

    def pop(self):
        if self.head is None:
            raise IndexError("List is empty!")
        retval = self.head.value
        self.head = self.head.next
        return retval

    def values(self):
        current = self.head
        while current != None:
            yield current.value
            current = current.next

    def nodes(self):
        current = self.head
        while current != None:
            yield current
            current = current.next

    def contains(self, target_value):
        for v in self.values:
            if v == target_value:
                return True
            return False

    def reverse(self):
        if not self.head:  ##empty
            return self.head
        previous = None
        current = self.head
        nxt = self.head.next
        while current:
            nxt = current.next
            current.next = previous
            previous = current  ##shift pointers
            current = nxt
        self.head = previous
        return self.head

    def __str__(self):
        return "(" + ",".join([str(v) for v in self.values()]) + ")"

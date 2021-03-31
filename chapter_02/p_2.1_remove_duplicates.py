'''
 Write code to remove duplicates from an unsorted linked list
 FOLLOW-UP: How would you solve this problem if a temporary buffer is not allowed?

Input: 1 -> 2 -> 1 -> 5 -> 2 -> None
Output: 1 -> 2 -> 5 -> None

'''

class Node(object):
    '''
    This is a Node class.
    '''

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):
        '''
        :param data: Node data
        :return: None
        '''
        node = Node(data)
        node.next = self.head
        self.head = node

    def display_list(self):
        current = self.head
        while current:
            print(current.value, end='->')
            current = current.next

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.value in dup_values:
                # Remove node
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before
                dup_values[cur.value] = 1
                prev = cur
            cur = prev.next


# test:

my_list = LinkedList()
my_list.insert_node(1)
my_list.insert_node(2)
my_list.insert_node(1)
my_list.insert_node(5)
my_list.insert_node(2)


print(my_list.display_list())       # print original list (with dups)
my_list.remove_duplicates()         # remove duplicates
print(my_list.display_list())       # print updated list (without dups)

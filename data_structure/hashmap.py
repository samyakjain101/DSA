class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashMap:

    def __init__(self):
        self.__size = 4
        self.__storage = [None]*self.__size

    def hash_function(self, key):
        return hash(key) % self.__size

    def put(self, key, value):
        new_node = Node(key=key, value=value, next=None)
        hash_index = self.hash_function(key)
        if self.__storage[hash_index] is None:
            self.__storage[hash_index] = new_node
        else:
            # Update if already exists, else add at end
            node = self.__storage[hash_index]
            while node.next is not None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next

            if node.key == key:
                node.value = value
                return

            node.next = new_node

    def get(self, key):
        hash_index = self.hash_function(key)
        node = self.__storage[hash_index]

        if node is None:
            raise KeyError
        else:
            while node.next is not None:
                if node.key == key:
                    return node.value

                node = node.next

            if node.key == key:
                return node.value
            else:
                raise KeyError

    def remove(self, key):
        hash_index = self.hash_function(key)
        node = self.__storage[hash_index]

        if node is None:
            raise KeyError
        else:
            temp_node = None
            while node.next is not None:
                if node.key == key:
                    if temp_node is not None:
                        temp_node.next = node.next
                    else:
                        self.__storage[hash_index] = None
                    node.next = None
                    return

                temp_node = node
                node = node.next

            if node.key == key:
                if temp_node is not None:
                    temp_node.next = node.next
                else:
                    self.__storage[hash_index] = None
                node.next = None
                return
            else:
                raise KeyError

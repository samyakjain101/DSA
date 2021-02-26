class StackEmpty(Exception):
    def __init__(self, message='Stack is Empty'):
        self.message = message
        super().__init__(self.message)


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.__root = None
        self.__length = 0

    def __increase_length(self):
        self.__length += 1

    def __decrease_length(self):
        self.__length -= 1

    def __empty_check(self):
        if self.__root is None:
            raise StackEmpty()

    def push(self, data=None):
        if self.__root is None:
            self.__root = Node(data=data)
        else:
            self.__root = Node(data=data, next=self.__root)

        self.__increase_length()

    def pop(self):
        self.__empty_check()
        top = self.__root.data
        self.__root = self.__root.next

        self.__decrease_length()
        return top

    def top(self):
        self.__empty_check()
        return self.__root.data

    def size(self):
        return self.__length

    def show(self):
        temp = self.__root
        while temp:
            print(temp.data)
            temp = temp.next

import pathmagic # noqa
from data_structure.stack import Stack


def insert_at_bottom(stack, end):
    if stack.size() == 0:
        stack.push(end)
        return
    last = stack.pop()
    insert_at_bottom(stack, end)
    stack.push(last)


def reverse_a_stack(stack):
    if stack.size() == 0:
        return
    end = stack.pop()
    reverse_a_stack(stack)
    insert_at_bottom(stack, end)


if __name__ == "__main__":
    stack = Stack()
    arr = [1, 2, 3, 4, 5]
    for num in arr:
        stack.push(num)
    reverse_a_stack(stack)
    stack.show()

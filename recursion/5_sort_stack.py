import pathmagic # noqa
from data_structure.stack import Stack


def insert(stack, last):
    if stack.size() == 0 or stack.top() <= last:
        stack.push(last)
        return
    end = stack.pop()
    insert(stack, last)
    stack.push(end)


def sort_stack(stack):
    if stack.size() == 1:
        return
    last = stack.pop()
    sort_stack(stack)
    insert(stack, last)


if __name__ == "__main__":
    stack = Stack()
    arr = [52, 0, -63, 4, 0, 99, 4, -514651651, 651465165162, 556, -5654]
    for num in arr:
        stack.push(num)
    sort_stack(stack)
    stack.show()

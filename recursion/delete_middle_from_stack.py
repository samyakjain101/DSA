import pathmagic # noqa
from data_structure.stack import Stack


def delete_middle_from_stack(stack, middle):
    if stack.size() == middle:
        stack.pop()
        return
    end = stack.pop()
    delete_middle_from_stack(stack, middle)
    stack.push(end)


if __name__ == "__main__":
    stack = Stack()
    arr = [1, 2, 3, 4, 5]
    for num in arr:
        stack.push(num)
    middle = int(stack.size()/2) + 1
    delete_middle_from_stack(stack, middle)
    stack.show()

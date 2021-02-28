def tower_of_hanoi(n: int, source: str, destination: str, helper: str):
    if n == 1:
        print(f'Move plate {n} from {source} to {destination}')
        return
    tower_of_hanoi(n-1, source, helper, destination)
    print(f'Move plate {n} from {source} to {destination}')
    tower_of_hanoi(n-1, helper, destination, source)


if __name__ == "__main__":
    tower_of_hanoi(3, 'source', 'destination', 'helper')

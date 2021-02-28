def powerset(input, output, result=set()):
    if len(input) == 0:
        result.add(output)
        return
    powerset(input[1:], output + "", result)
    powerset(input[1:], output + input[0], result)
    return result


if __name__ == "__main__":
    print(powerset("abcd", ""))

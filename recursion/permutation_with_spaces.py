def permutation_with_spaces(input, output):
    if len(input) == 0:
        print(output)
        return
    permutation_with_spaces(input[1:], output + '_' + input[0])
    permutation_with_spaces(input[1:], output + input[0])


if __name__ == "__main__":
    input = 'ABC'
    output = ''
    permutation_with_spaces(input[1:], input[0])

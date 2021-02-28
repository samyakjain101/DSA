def permutation_with_case_change(input, output):
    if len(input) == 0:
        print(output)
        return
    permutation_with_case_change(input[1:], output + input[0].lower())
    permutation_with_case_change(input[1:], output + input[0].upper())


if __name__ == "__main__":
    input = 'AB'
    output = ''
    permutation_with_case_change(input, output)

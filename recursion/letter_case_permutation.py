def letter_case_permutation(input, output):
    if len(input) == 0:
        print(output)
        return
    if input[0].isdigit():
        return letter_case_permutation(input[1:], output + input[0])
    letter_case_permutation(input[1:], output + input[0].lower())
    letter_case_permutation(input[1:], output + input[0].upper())


if __name__ == "__main__":
    input = 'a1b2'
    output = ''
    letter_case_permutation(input, output)

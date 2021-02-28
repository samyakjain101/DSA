def generate_all_balanced_paranthesis(output, open, close):
    if open == close == 0:
        print(output)
        return
    if open != 0:
        generate_all_balanced_paranthesis(output+'(', open-1, close)
    if close > open:
        generate_all_balanced_paranthesis(output+')', open, close-1)


if __name__ == "__main__":
    n = open = close = 3
    output = ''
    generate_all_balanced_paranthesis(output, open, close)

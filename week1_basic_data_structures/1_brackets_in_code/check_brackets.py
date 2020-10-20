# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((i, next))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i+1
            else:
                cur = opening_brackets_stack[-1][1]
                if (next == ')' and cur!='(') or (next == '}' and cur!='{') or (next == ']' and cur!='['):
                    return i+1
                else:
                    opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[-1][0]+1
    return -1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == -1:
        print('Success')
    else:
        print(mismatch)

if __name__ == "__main__":
    main()

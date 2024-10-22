def is_closed(parenthesis):
    test_stack = []
    for char in parenthesis:
        if char in ["(", "["]:
            test_stack.append(char)
        else:
            if len(test_stack) == 0:
                return False
            else:
                from_stack = test_stack.pop()
                if (from_stack == "(" and char != ")") or (from_stack == "[" and char != "]"):
                    return False

    return len(test_stack) == 0

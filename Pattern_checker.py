def is_pattern_valid(expression):
    stack = []
    a_count = 0
    b_count = 0
    c_count = 0
    state = 0  # 0: counting a's, 1: counting b's, 2: counting c's

    for char in expression:
        if state == 0:  # Counting a's
            if char == 'a':
                a_count += 1
                stack.append(char)
            elif char == 'b':
                if a_count == 0:
                    return False
                state = 1
                b_count += 1
                stack.append(char)
            else:
                return False
        elif state == 1:  # Counting b's
            if char == 'b':
                b_count += 1
                stack.append(char)
            elif char == 'c':
                if a_count == 0 and b_count < a_count:  # Pattern 1/2 check
                    return False
                state = 2
                c_count += 1
                stack.append(char)
            else:
                return False
        else:  # Counting c's
            if char == 'c':
                c_count += 1
                stack.append(char)
            else:
                return False

    # Validate patterns after scanning
    if state == 2:  # Reached c's
        # Pattern 1: N a's, N b's, any c's
        if a_count == b_count:
            return True
        # Pattern 2: N a's, any b's, N c's
        if a_count == c_count:
            return True
        # Pattern 3: Any a's, N b's, N c's
        if b_count == c_count:
            return True
    return False

# Test cases
test_expressions = [
    "aaabbbccc",    # Pattern 1: N a's, N b's, any c's
    "aabcc",        # Pattern 2: N a's, any b's, N c's
    "aaaabbbccc",   # Pattern 3: Any a's, N b's, N c's
    "ab",           # Invalid
    "aaabbc",       # Invalid
    "abc"           # Invalid
]

for expr in test_expressions:
    result = is_pattern_valid(expr)
    print(f"Expression {expr}: {'Valid' if result else 'Invalid'}")
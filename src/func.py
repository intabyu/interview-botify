from typing import List


def f(s: str) -> bool:
    close_to_open = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    opening_chars = "".join(close_to_open.values())
    closing_chars = "".join(close_to_open.keys())
    chars = opening_chars + closing_chars

    stack: List[str] = []

    for c in s:
        if c not in chars:
            continue

        last = None
        if len(stack) > 0:
            last = stack[-1]

        if c in opening_chars:
            stack.append(c)
        elif c in closing_chars:
            if last != close_to_open[c]:
                return False
            else:
                stack.pop()

    return len(stack) == 0  # if stack is empty then everything got closed correctly
